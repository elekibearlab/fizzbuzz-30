"""Build compare.html: a single-file page that shows selected FizzBuzz sources side by side."""

import base64
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
OUT = ROOT / "compare.html"
TEMPLATE = HERE / "compare.template.html"
VERSIONS = ("aligned", "idiomatic")

# highlight.js language name per slug (None = plain text)
# Batch uses dos; compare.template.html loads its extra language module.
HLJS = {
    "c": "c", "cpp": "cpp", "csharp": "csharp", "java": "java", "python": "python",
    "javascript": "javascript", "go": "go", "rust": "rust", "php": "php", "ruby": "ruby",
    "kotlin": "kotlin", "swift": "swift", "lua": "lua", "bash": "bash", "batch": "dos",
    "powershell": "powershell", "r": "r", "julia": "julia", "fortran": "fortran",
    "gdscript": None, "cobol": None, "sql": "sql", "asm": "x86asm", "commonlisp": "lisp",
    "scheme": "scheme", "haskell": "haskell", "elixir": "elixir", "erlang": "erlang",
    "prolog": "prolog", "brainfuck": "brainfuck",
}


def read_csv(name):
    with open(ROOT / "data" / name, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def find_source(slug, version):
    matches = sorted((ROOT / "languages" / slug).glob(version + ".*"))
    if len(matches) != 1:
        raise SystemExit(f"{slug}/{version}: expected 1 file, found {len(matches)}")
    return matches[0]


def main():
    stats = {(r["slug"], r["version"]): r for r in read_csv("stats.csv")}
    languages = []
    for row in read_csv("languages.csv"):
        slug = row["slug"]
        logo = None
        if row["logo_file"]:
            svg = (ROOT / row["logo_file"]).read_bytes()
            logo = "data:image/svg+xml;base64," + base64.b64encode(svg).decode("ascii")
        sources = {}
        for version in VERSIONS:
            path = find_source(slug, version)
            st = stats.get((slug, version), {})
            sources[version] = {
                "file": path.relative_to(ROOT).as_posix(),
                "code": path.read_text(encoding="utf-8").replace("\r\n", "\n"),
                "lines": int(st["lines"]) if st.get("lines") else None,
                "chars": int(st["chars"]) if st.get("chars") else None,
            }
        languages.append({
            "slug": slug,
            "name": row["name"],
            "year": int(row["year"]),
            "designer": row["designer"],
            "logo": logo,
            "hljs": HLJS.get(slug),
            "sources": sources,
        })

    data = json.dumps(languages, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/[]", data)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"wrote {OUT.name} ({len(languages)} languages)")


if __name__ == "__main__":
    main()
