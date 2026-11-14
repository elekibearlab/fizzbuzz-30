from pathlib import Path
import csv
import datetime
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
os.chdir(root)
build = root / '.build'
build.mkdir(exist_ok=True)
extensions = dict(zip(
    'c cpp csharp java python javascript go rust php ruby '
    'kotlin swift scala lua bash powershell r julia fortran '
    'gdscript cobol sql asm commonlisp scheme haskell '
    'elixir erlang prolog brainfuck'.split(),
    'c cpp cs java py js go rs php rb kt swift scala lua sh '
    'ps1 R jl f90 gd cob sql asm lisp scm hs exs erl pl bf'.split()
))
versions = {
    'c': 'gcc --version',
    'cpp': 'g++ --version',
    'csharp': 'mcs --version',
    'java': 'java -version',
    'python': 'python3 --version',
    'javascript': 'node --version',
    'go': 'go version',
    'rust': 'rustc --version',
    'php': 'php --version',
    'ruby': 'ruby --version',
    'kotlin': 'kotlinc -version',
    'swift': 'swiftc --version',
    'scala': 'scalac -version',
    'lua': 'lua5.4 -v',
    'bash': 'bash --version',
    'powershell': 'pwsh --version',
    'r': 'Rscript --version',
    'julia': 'julia --version',
    'fortran': 'gfortran --version',
    'gdscript': 'godot --version',
    'cobol': 'cobc --version',
    'sql': 'sqlite3 --version',
    'asm': 'nasm -v',
    'commonlisp': 'sbcl --version',
    'scheme': 'guile --version',
    'haskell': 'ghc --version',
    'elixir': 'elixir --version',
    'erlang': 'erl -noshell -eval',
    'prolog': 'swipl --version',
    'brainfuck': 'bf -h',
}

def commands(slug, version, source, target):
    binary = str(target / 'program')
    source = str(source)
    folder = str(target)
    if slug in ('c', 'cpp', 'rust', 'fortran'):
        compiler = {
            'c': ['gcc', '-std=c11', '-Wall', '-Wextra'],
            'cpp': ['g++', '-std=c++20', '-Wall', '-Wextra'],
            'rust': ['rustc', '--edition=2021'],
            'fortran': ['gfortran', '-std=f2008', '-Wall'],
        }[slug]
        return [compiler + [source, '-o', binary]], [binary]
    if slug == 'csharp':
        return [['mcs', source, '-out:' + binary]], [
            'mono', binary
        ]
    if slug == 'java':
        return [['javac', '-d', folder, source]], [
            'java', '-cp', folder, 'Main'
        ]
    if slug == 'go':
        return [['go', 'build', '-o', binary, source]], [binary]
    if slug == 'kotlin':
        jar = str(target / 'program.jar')
        return [[
            'kotlinc', source, '-include-runtime', '-d', jar
        ]], ['java', '-jar', jar]
    if slug == 'swift':
        return [[
            'swiftc', '-module-cache-path',
            str(build / 'swift-cache'), source, '-o', binary
        ]], [binary]
    if slug == 'scala':
        return [['scalac', '-d', folder, source]], [
            'scala', '-cp', folder, 'Main'
        ]
    if slug == 'cobol':
        return [['cobc', '-x', '-free', source, '-o', binary]], [binary]
    if slug == 'asm':
        obj = str(target / 'program.o')
        compile_steps = [['nasm', '-f', 'elf64', source, '-o', obj]]
        compile_steps.append(
            ['gcc', '-no-pie', obj, '-o', binary]
            if version == 'aligned' else
            ['ld', obj, '-o', binary]
        )
        return compile_steps, [binary]
    if slug == 'haskell':
        return [[
            'ghc', '-outputdir', folder, source, '-o', binary
        ]], [binary]
    if slug == 'erlang':
        return [['erlc', '-o', folder, source]], [
            'erl', '-noshell', '-pa', folder,
            '-s', version, 'main', '-s', 'init', 'stop'
        ]
    interpreters = {
        'python': ['python3', '-B'],
        'javascript': ['node'],
        'php': ['php'],
        'ruby': ['ruby'],
        'lua': ['lua5.4'],
        'bash': ['bash'],
        'powershell': ['pwsh', '-NoLogo', '-NoProfile', '-File'],
        'r': ['Rscript', '--vanilla'],
        'julia': ['julia', '--startup-file=no'],
        'gdscript': ['godot', '--headless', '-s'],
        'sql': ['sqlite3', '-batch', '-noheader', ':memory:'],
        'commonlisp': ['sbcl', '--script'],
        'scheme': ['guile', '--no-auto-compile', '-s'],
        'elixir': ['elixir'],
        'prolog': ['swipl', '-q', '-s'],
        'brainfuck': ['bf'],
    }
    return [], interpreters[slug] + ([] if slug == 'sql' else [source])

def execute(command, target, label, input_bytes=None):
    with (target / 'commands.txt').open('a') as handle:
        handle.write(shlex.join(command) + '\n')
    result = subprocess.run(
        command, input=input_bytes, capture_output=True,
        timeout=180, cwd=target
    )
    (target / f'{label}.stdout').write_bytes(result.stdout)
    (target / f'{label}.stderr').write_bytes(result.stderr)
    if result.returncode:
        raise RuntimeError(f'{label}: exit {result.returncode}')
    return result.stdout

version_rows = []
missing = []
for slug, command in versions.items():
    args = shlex.split(command)
    if slug == 'erlang':
        args += [
            'io:format("OTP ~s / ERTS ~s~n", '
            '[erlang:system_info(otp_release), '
            'erlang:system_info(version)]), halt().'
        ]
    if not shutil.which(args[0]):
        version_rows.append((slug, 'UNAVAILABLE: ' + args[0]))
        missing.append(slug)
        continue
    result = subprocess.run(args, capture_output=True, timeout=30)
    info = (result.stdout + result.stderr).decode(errors='replace')
    lines = [s.strip() for s in info.splitlines() if s.strip()]
    if slug == 'kotlin':
        lines = [s for s in lines if 'kotlinc' in s]
    if slug == 'elixir':
        lines = [s for s in lines if 'Elixir' in s or 'Erlang' in s]
    version_rows.append((slug, ' / '.join(lines[:2])))

results = []
stats = []
expected = (root / 'data' / 'expected.txt').read_bytes()
assert len(expected.splitlines()) == 100
for slug, ext in extensions.items():
    for version in ('aligned', 'idiomatic'):
        source = root / 'languages' / slug / f'{version}.{ext}'
        text = source.read_text(encoding='utf-8')
        lines = sum(bool(s.strip()) for s in text.splitlines())
        stats.append((slug, version, lines,
                      sum(not c.isspace() for c in text)))
        target = build / slug / version
        target.mkdir(parents=True, exist_ok=True)
        (target / 'commands.txt').write_text('')
        detail = ''
        status = 'NG'
        try:
            if slug in missing:
                raise RuntimeError('Runtime unavailable')
            if slug not in ('brainfuck', 'cobol', 'asm'):
                if version == 'aligned' and len(text.splitlines()) > 25:
                    raise RuntimeError('Aligned source exceeds 25 lines')
            steps, run = commands(slug, version, source, target)
            for index, command in enumerate(steps):
                execute(command, target, f'build-{index}')
            output = execute(
                run, target, 'run',
                source.read_bytes() if slug == 'sql' else None
            )
            if slug == 'gdscript':
                output = re.sub(
                    rb'\AGodot Engine v[^\n]*\n(?:[ \t]*\n)?',
                    b'', output
                )
            actual = target / 'actual.txt'
            actual.write_bytes(output)
            difference = subprocess.run(
                ['diff', '-u', str(root / 'data' / 'expected.txt'), str(actual)],
                capture_output=True
            )
            (target / 'diff.txt').write_bytes(difference.stdout)
            if difference.returncode:
                raise RuntimeError('Output differs from expected.txt')
            status = 'OK'
        except Exception as error:
            detail = str(error).replace('|', '/')
        results.append((slug, version, status, detail))
        print(f'{slug}/{version}: {status} {detail}', flush=True)

with (root / 'data' / 'stats.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('slug', 'version', 'lines', 'chars'))
    writer.writerows(stats)

ok = sum(row[2] == 'OK' for row in results)
report = [
    '# Execution results', '',
    f'UTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}',
    f'Platform: {platform.platform()}', '',
    f'OK: {ok} / NG: {60 - ok}', '',
    '| slug | version | result | detail |',
    '| --- | --- | --- | --- |',
]
report += [f'| {s} | {v} | {r} | {d} |' for s, v, r, d in results]
report += ['', '## Runtime versions', '',
           '| slug | runtime |', '| --- | --- |']
report += [f'| {s} | {v.replace(chr(124), chr(47))} |'
           for s, v in version_rows]
report += [
    '', '## Unavailable runtimes', '',
    ', '.join(missing) if missing else 'None.', '',
    '## Verification', '',
    'Each source is built independently and executed with a 180-second',
    'timeout. Its output is compared byte-for-byte using diff -u.',
    'Build commands, stdout, stderr and diffs remain in .build/.',
    'Only the Godot startup banner is removed before comparison.',
    'SQL runs in a fresh in-memory SQLite database.',
    'Brainfuck runs with unsigned 8-bit wrapping cells.', '',
    'stats.csv counts nonempty lines and Unicode characters other',
    'than whitespace. Source files contain no comments.', '',
]
(root / 'docs' / 'results.md').write_text(
    '\n'.join(report), encoding='utf-8', newline='\n'
)
sys.exit(0 if ok == 60 else 1)
