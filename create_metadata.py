from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import csv
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
cache = root / '.downloads' / 'metadata'
cache.mkdir(parents=True, exist_ok=True)
logos = root / 'logos'
logos.mkdir(exist_ok=True)

def fetch(url):
    path = cache / hashlib.sha256(url.encode()).hexdigest()
    if not path.exists():
        request = urllib.request.Request(url, headers={
            'User-Agent': 'FizzBuzz30/1.0 (language reference research)'
        })
        with urllib.request.urlopen(request, timeout=60) as response:
            path.write_bytes(response.read())
    return path.read_bytes()

data = [
    ('c', 'C', 1972, 'Dennis Ritchie', 'C_(programming_language)'),
    ('cpp', 'C++', 1985, 'Bjarne Stroustrup', 'C++'),
    ('csharp', 'C#', 2000, 'Anders Hejlsberg', 'C_Sharp_(programming_language)'),
    ('java', 'Java', 1995, 'James Gosling', 'Java_(programming_language)'),
    ('python', 'Python', 1991, 'Guido van Rossum', 'Python_(programming_language)'),
    ('javascript', 'JavaScript', 1995, 'Brendan Eich', 'JavaScript'),
    ('go', 'Go', 2009, 'Robert Griesemer; Rob Pike; Ken Thompson', 'Go_(programming_language)'),
    ('rust', 'Rust', 2012, 'Graydon Hoare', 'Rust_(programming_language)'),
    ('php', 'PHP', 1995, 'Rasmus Lerdorf', 'PHP'),
    ('ruby', 'Ruby', 1995, 'Yukihiro Matsumoto', 'Ruby_(programming_language)'),
    ('kotlin', 'Kotlin', 2011, 'Andrey Breslav; JetBrains', 'Kotlin_(programming_language)'),
    ('swift', 'Swift', 2014, 'Chris Lattner; Doug Gregor; John McCall; Ted Kremenek; Joe Groff; Apple', 'Swift_(programming_language)'),
    ('scala', 'Scala', 2004, 'Martin Odersky', 'Scala_(programming_language)'),
    ('lua', 'Lua', 1993, 'Roberto Ierusalimschy; Waldemar Celes; Luiz Henrique de Figueiredo', 'Lua_(programming_language)'),
    ('bash', 'Bash', 1989, 'Brian Fox', 'Bash_(Unix_shell)'),
    ('powershell', 'PowerShell', 2006, 'Jeffrey Snover; Bruce Payette; James Truher', 'PowerShell'),
    ('r', 'R', 1993, 'Ross Ihaka; Robert Gentleman', 'R_(programming_language)'),
    ('julia', 'Julia', 2012, 'Jeff Bezanson; Stefan Karpinski; Viral B. Shah; Alan Edelman', 'Julia_(programming_language)'),
    ('fortran', 'Fortran', 1957, 'John Backus', 'Fortran'),
    ('gdscript', 'GDScript', 2014, 'Juan Linietsky; Ariel Manzur', 'Godot_(game_engine)'),
    ('cobol', 'COBOL', 1960, 'Howard Bromberg; Norman Discount; Vernon Reeves; Jean E. Sammet; William Selden; Gertrude Tierney (CODASYL)', 'COBOL'),
    ('sql', 'SQL', 1973, 'Donald D. Chamberlin; Raymond F. Boyce', 'SQL'),
    ('asm', 'Assembly (x86-64 Linux; NASM)', 1947, 'Kathleen Booth', 'Assembly_language'),
    ('commonlisp', 'Common Lisp', 1984, 'Scott Fahlman; Richard P. Gabriel; David A. Moon; Kent Pitman; Guy L. Steele Jr.; Daniel Weinreb', 'Common_Lisp'),
    ('scheme', 'Scheme', 1975, 'Guy L. Steele Jr.; Gerald Jay Sussman', 'Scheme_(programming_language)'),
    ('haskell', 'Haskell', 1990, 'Simon Peyton Jones; Paul Hudak; Philip Wadler; et al.', 'Haskell'),
    ('elixir', 'Elixir', 2012, 'José Valim', 'Elixir_(programming_language)'),
    ('erlang', 'Erlang', 1986, 'Joe Armstrong; Robert Virding; Mike Williams', 'Erlang_(programming_language)'),
    ('prolog', 'Prolog', 1972, 'Alain Colmerauer; Robert Kowalski', 'Prolog'),
    ('brainfuck', 'Brainfuck', 1993, 'Urban Müller', 'Brainfuck'),
]

commit = json.loads(fetch(
    'https://api.github.com/repos/devicons/devicon/commits/master'
))['sha']
base = f'https://raw.githubusercontent.com/devicons/devicon/{commit}/'
icons = {icon['name']: icon for icon in json.loads(fetch(base + 'devicon.json'))}
mapping = {'cpp': 'cplusplus', 'gdscript': 'godot', 'asm': 'nasm',
           'commonlisp': 'commonlisp'}

def plain(value):
    value = re.sub(r'<style\b.*?</style>', '', value, flags=re.S)
    value = re.sub(r'<sup\b.*?</sup>', '', value, flags=re.S)
    value = re.sub(r'<[^>]+>', ' ', value)
    return ' '.join(html.unescape(value).split())

def collect(row):
    slug, name, year, designer, page = row
    wiki = 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(page)
    try:
        document = fetch(wiki).decode()
        info = []
        for tr in re.findall(r'<tr\b.*?</tr>', document, re.S):
            label = plain(tr)
            if any(key in label for key in (
                'First appeared', 'Designed by', 'Initial release',
                'Original authors'
            )):
                info.append(label[:600])
        evidence = '; '.join(info[:4])
    except Exception as error:
        evidence = 'Fetch failed: ' + str(error)
    icon_name = mapping.get(slug, slug)
    logo_file = logo_source = license_name = ''
    if icon_name in icons:
        variants = icons[icon_name]['versions']['svg']
        variant = 'original' if 'original' in variants else None
        if variant is not None:
            logo_source = base + f'icons/{icon_name}/{icon_name}-{variant}.svg'
            content = fetch(logo_source)
            assert ET.fromstring(content).tag.endswith('svg')
            logo_file = f'logos/{slug}.svg'
            (root / logo_file).write_bytes(content)
            license_name = 'MIT'
    if slug == 'commonlisp' and not logo_file:
        logo_source = (
            'https://lisp-lang.org/assets/img/favicon/'
            'generated/safari-pinned-tab.svg'
        )
        content = fetch(logo_source)
        assert ET.fromstring(content).tag.endswith('svg')
        logo_file = 'logos/commonlisp.svg'
        (root / logo_file).write_bytes(content)
        license_name = 'Not specified by source'
    print(slug + ': ' + evidence, flush=True)
    return (slug, name, year, designer, logo_file,
            logo_source, license_name), (slug, wiki, evidence)

with ThreadPoolExecutor(max_workers=6) as pool:
    collected = list(pool.map(collect, data))

with (root / 'languages.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('slug', 'name', 'year', 'designer', 'logo_file',
                     'logo_source_url', 'license'))
    writer.writerows(row for row, _ in collected)

(logos / 'DEVICON-LICENSE.txt').write_bytes(fetch(base + 'LICENSE'))
sources = [
    '# Language metadata sources', '',
    'The license column describes the logo asset license.',
    f'Devicon revision: {commit}.',
    '[Devicon repository](https://github.com/devicons/devicon)', '',
    'Years use first public appearance, rather than version 1.0.',
    'Assembly year/designer refer to the language family, not NASM',
    'or the later x86-64 architecture. Its logo is NASM.',
    'GDScript uses Godot public',
    'release in 2014 and its project authors. Its logo is Godot.',
    'Blank logo fields mean no eligible SVG was located.', '',
    'COBOL uses the English Wikipedia first-appearance value (1960),',
    'rather than its 1959 design year. SQL likewise uses that',
    'infobox value (1973). Common Lisp uses the SVG favicon served',
    'by lisp-lang.org; that source does not specify an asset license.', '',
    '| slug | source | retrieved infobox |',
    '| --- | --- | --- |',
]
sources += [f'| {s} | [English Wikipedia]({u}) | {e.replace(chr(124), chr(47))} |'
            for _, (s, u, e) in collected]
sources += [
    '', '## Logo search without a matching SVG', '',
    '- SQL: Devicon has vendor/product logos, not a general SQL logo.',
    '- Scheme: no Devicon entry or SVG logo on [scheme.org](https://www.scheme.org/).',
    '- Brainfuck: no Devicon entry or SVG logo on [brainfuck.org](https://www.brainfuck.org/).',
]
(root / 'metadata_sources.md').write_text(
    '\n'.join(sources) + '\n', encoding='utf-8', newline='\n'
)
