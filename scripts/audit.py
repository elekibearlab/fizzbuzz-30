from pathlib import Path
import csv
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent.parent
with (root / 'data' / 'languages.csv').open(encoding='utf-8') as f:
    languages = list(csv.DictReader(f))
assert len(languages) == 30
assert len({row['slug'] for row in languages}) == 30
sources = []
for row in languages:
    slug = row['slug']
    for version in ('aligned', 'idiomatic'):
        matches = list((root / 'languages' / slug).glob(version + '.*'))
        assert len(matches) == 1, (slug, version)
        source = matches[0]
        sources.append(source)
        text = source.read_text(encoding='utf-8')
        assert '\r' not in text
        assert text.endswith('\n')
        for index, line in enumerate(text.splitlines(), 1):
            assert len(line) <= 60, (source, index, len(line))
            if slug != 'go':
                assert '\t' not in line, (source, index)
                indent = len(line) - len(line.lstrip(' '))
                assert indent % 4 == 0, (source, index, indent)
        if slug not in ('brainfuck', 'cobol', 'asm'):
            if version == 'aligned':
                assert len(text.splitlines()) <= 25, source
        if slug == 'brainfuck':
            assert not re.sub(r'[<>+.,\[\]\-\s]', '', text)
    if row['logo_file']:
        image = ET.parse(root / row['logo_file']).getroot()
        assert image.tag == '{http://www.w3.org/2000/svg}svg'
        assert row['logo_source_url'].startswith('https://')
        assert row['license']

with (root / 'data' / 'stats.csv').open(encoding='utf-8') as f:
    stats = list(csv.DictReader(f))
assert len(stats) == 60
for source in sources:
    slug = source.parent.name
    version = source.stem
    row, = [r for r in stats if r['slug'] == slug
            and r['version'] == version]
    text = source.read_text(encoding='utf-8')
    assert int(row['lines']) == sum(
        bool(line.strip()) for line in text.splitlines()
    )
    assert int(row['chars']) == sum(
        not char.isspace() for char in text
    )

print('Sources: 60; metadata: 30; stats: 60')
print('Line widths, indentation, aligned limits and SVGs: OK')
