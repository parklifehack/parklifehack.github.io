# parklifehack.github.io

GitHub Pagesで公開する、小さい個人用の静的サイトです。

## 構成

```text
.
├── index.html
├── style.css
├── images/
└── README.md
```

## 写真を置く

最初の写真は、`images/main.jpg` として置いています。

写真を差し替えるときは、新しい画像を同じ名前で置き換えます。

## トピック

トップの短い文章内の言葉だけをリンクにしています。

* `パン` → `#bread`
* `写真` → `#photos`
* `言葉` → `#words`
* `ハガキ` → `#postcards`
* `ビート` → `#beats`

今は同じページ内の小さな入口です。内容が増えてきたら、個別ページに分けられます。

## 公開方法

このリポジトリ名が `parklifehack.github.io` なら、`main` ブランチへpushするとGitHub Pagesで公開できます。

公開URL:

```text
https://parklifehack.github.io/
```

もし公開されない場合:

1. GitHubでこのリポジトリを開く
2. `Settings` を開く
3. 左メニューの `Pages` を開く
4. `Build and deployment` の `Source` を `Deploy from a branch` にする
5. `Branch` を `main`、フォルダを `/root` にする
6. `Save` を押す

数十秒から数分で公開されます。
