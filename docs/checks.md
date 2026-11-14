# 検査の中身

## verify.py（`scripts/run_all.sh` から呼ばれる）

- 60 本をそれぞれ別にビルド・実行し、出力を `data/expected.txt` とバイト単位で比べる（`diff -u`）
- Godot のエンジン起動バナーだけは、比べる前に取り除く
- 結果を `docs/results.md`、行数と文字数を `data/stats.csv` に書き出す

## audit.py

- ソースが 60 本、言語データが 30 行あること
- 1 行は 60 桁以内
- 字下げはスペース 4 個（Go だけは `gofmt` のタブ）
- aligned は 25 行以内（空行も含める。Brainfuck・COBOL・Assembly は除く）
- Brainfuck のソースには命令の 8 文字と空白しかないこと
- ロゴが SVG で、出典 URL とライセンスが記録されていること
- `data/stats.csv` の数がソースと合っていること（行数は空行を除く、文字数は空白文字を除く）

## そのほかのスクリプト

- `create_brainfuck.py`: Brainfuck のソースを作り直す
- `create_metadata.py`: 言語データの出典を確かめ、ロゴを取り直す（出典は `docs/metadata_sources.md`）
