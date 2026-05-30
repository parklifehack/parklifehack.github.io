# parklifehack.github.io

GitHub Pagesで公開する、小さい個人用の静的サイトです。

## 構成

```text
.
├── index.html
├── style.css
├── images/
├── bread/
├── photos/
├── words/
├── postcards/
├── beats/
└── README.md
```

## 写真を置く

最初の写真は、`images/main.jpg` として置いています。

写真を差し替えるときは、新しい画像を同じ名前で置き換えます。

## トピック

トップの短い文章内の言葉だけをリンクにしています。

* `パン` → `/bread/`
* `写真` → `/photos/`
* `言葉` → `/words/`
* `ハガキ` → `/postcards/`
* `ビート` → `/beats/`

それぞれ独立したページです。投稿が増えたら、各ページ内の `.entry-list` に `<article class="entry">` を追加します。

## 名前とURL

サイト上の表示名は `parklifeduck` にしています。

GitHub PagesのURLはGitHubユーザー名とリポジトリ名に連動します。今の公開URLは:

```text
https://parklifehack.github.io/
```

URL自体を `https://parklifeduck.github.io/` にしたい場合は、GitHubのユーザー名を `parklifeduck` に変更し、リポジトリ名も `parklifeduck.github.io` に変更します。

ユーザー名を変えない場合は、独自ドメインを使う方法もあります。

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
