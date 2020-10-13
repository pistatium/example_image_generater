# Python で文字を画像として出力するサンプル

pillow ライブラリを使って、任意の入力文字列を画像(PNG)として出力するためのサンプルプログラムです。

## セットアップ

```sh
pip3 install -r requirements.txt
```

## 動かし方

```sh
python3 main.py "山路を登りながら"
```

※ `OSError: cannot open resource` が出る場合は、動作環境に応じて適切な FONT_PATHを指定してください。
任意のフォントを使うことが出来ます。日本語を出力したい場合は日本語のフォントを使ってください。


