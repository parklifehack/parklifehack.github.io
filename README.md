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

最初の写真は、`images/main.jpg` として置く想定です。

写真を追加したら、`index.html` の `.photo-slot` を `<img>` に差し替えます。

例:

```html
<img class="main-photo" src="images/main.jpg" alt="焼いたパンの写真">
```

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
