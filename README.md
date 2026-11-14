# FizzBuzz in 30 languages

各言語に `aligned`（比較用の同じ判定順）と `idiomatic`（言語ごとの書き方）を置いています。
どちらも 1〜100 を 1 行ずつ出力します。コードにコメントはありません。

## 実行

WSL Ubuntu 22.04 の x86-64 環境を使用します。
このフォルダをカレントディレクトリにして実行します。

```sh
sudo bash setup.sh
python3 setup_portable.py
bash run_all.sh
```

`setup.sh` は apt で処理系と共有ライブラリをインストールします。
`setup_portable.py` は公式配布の Swift 5.10.1、Julia 1.10.10、
PowerShell 7.4.13、Godot 4.3 を `.runtimes/` に展開します。
個別の再導入は `python3 setup_portable.py godot` のように指定します。

`run_all.sh` は `verify.py` を呼び、60 本すべてを独立してビルド・実行し、
`expected.txt` と `diff -u` でバイト単位の比較を行います。
不一致またはビルド・実行失敗があれば終了コードは 1 です。
最後に `audit.py` でファイル数・統計・60 桁以内・字下げ・行数・SVG を検査します。
`results.md` と `stats.csv` は実行のたびに更新します。
実行コマンド・標準出力・標準エラー・差分は `.build/<slug>/<version>/` に残ります。
Godot のエンジン起動バナーだけは比較前に除きます。

## 比較上の扱い

`aligned` は 15 → 3 → 5 → 数字の順で判定し、ループから呼び出します。
SQL は SQLite の CASE 式が関数に相当します。
COBOL は文字列を設定する段落、Bash は標準出力を文字列の返り値として扱います。
Haskell の反復は `mapM_`、Prolog は `forall/2` を使います。
Brainfuck は 3 と 5 のカウントダウンと十進桁カウンタで判定する同一実装です。
`create_brainfuck.py` で同じソースを再生成できます。

空行を除く行数と、空白・改行などの空白文字を除く文字数は `stats.csv` に記録します。
`aligned` の 25 行制限は空行も含めて検証しています（指定の 3 言語を除く）。
Go のインデントは `gofmt`、それ以外のコードはスペース 4 個です。

## 比較ページ

`compare.html` をブラウザで開くと、選んだ言語のコードを横に並べて見比べられます。
`aligned` と `idiomatic` の切り替え、公開年順・名前順・行数順の並べ替えができます。
選択状態は URL の `#` 以降に入るので、そのまま共有できます
（例: `compare.html#v=aligned&l=c,python,cobol`）。

ソースとロゴは `compare.html` に埋め込んでいます。サーバーは不要です。
構文の色付けだけ cdnjs の highlight.js を読み込みます。
ソースや `languages.csv` を変更したら、次のコマンドで作り直します。

```sh
python3 build_compare.py
```

ページの見た目は `compare.template.html` で編集します。

## 言語データとロゴ

`languages.csv` に公開年・設計者・ロゴのファイル名と出典を収録しています。
年は英語版 Wikipedia の first appearance を基準にし、
設計年・規格制定年・バージョン 1.0 と区別しています。
参照ページと取得した根拠は `metadata_sources.md` に記録しました。
`create_metadata.py` は出典確認とロゴ取得の再実行用です。

ロゴは既存 SVG をそのまま保存しています。Devicon の original を優先し、
その MIT ライセンスは `logos/DEVICON-LICENSE.txt` に同梱しています。
Common Lisp は lisp-lang.org 配布の SVG を使用しています。
`license` 列は言語やコンパイラではなくロゴ素材のライセンスです。
SQL・Scheme・Brainfuck のロゴ欄は空です。

このフォルダは独立した Git リポジトリです。リモートは設定していません。
