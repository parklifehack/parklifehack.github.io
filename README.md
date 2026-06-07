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
├── books/
├── postcards/
├── beats/
│   ├── volume-1/
│   └── volume-2/
├── audio/
│   ├── beat-tape-volume-1/
│   └── beat-tape-volume-2/
└── README.md
```

## 写真を置く

最初の写真は、`images/main.jpg` として置いています。

写真を差し替えるときは、新しい画像を同じ名前で置き換えます。

## トピック

トップの短い文章内の言葉だけをリンクにしています。

* `パン` → `/bread/`
* `写真` → `/photos/`
* `本` → `/books/`
* `ハガキ` → `/postcards/`
* `ビート` → `/beats/`

それぞれ独立したページです。投稿が増えたら、各ページの一覧部分に行や記事を追加します。

## ハガキの記録を追加する

自分宛てのハガキは `/postcards/` に置きます。

写真は、住所・名前・郵便番号・バーコードなど個人情報が見えないように加工し、できればハガキ部分だけにクロップしてから、以下に置きます。

```text
images/postcards/card-001-back.jpg
```

記録する項目は、まず以下の4つです。

* 書いた日
* 郵便局で処理された日付と時間
* 処理場所の数字やコード
* 個人情報を隠した背面写真

`postcards/index.html` の `.postcard-table tbody` 内に、コメントで残している `<tr>` テンプレートをコピーして追加します。

## ビートテープに曲を追加する

ビートテープ用のページは以下です。

* `Beat Tape Volume 1` → `/beats/volume-1/`
* `Beat Tape Volume 2` → `/beats/volume-2/`

音源ファイルは以下に置きます。

* Volume 1: `audio/beat-tape-volume-1/`
* Volume 2: `audio/beat-tape-volume-2/`

ファイル名は、スペースなしの半角英数字にします。

```text
audio/beat-tape-volume-1/01-night-loop.mp3
audio/beat-tape-volume-1/02-window-light.mp3
```

曲をページに表示するには、該当する `beats/volume-1/index.html` または `beats/volume-2/index.html` の `.track-list` 内に、以下の形で追加します。

```html
<article class="track">
  <div class="track-text">
    <span class="entry-label">track 01</span>
    <h2>Night Loop</h2>
    <p>1:12 / 2026</p>
  </div>
  <audio controls preload="none" src="../../audio/beat-tape-volume-1/01-night-loop.mp3"></audio>
</article>
```

WAVはサイズが大きくなりやすいので、公開用はMP3かM4Aがおすすめです。GitHubは大きいファイルに向いていないため、1曲あたり数MBから十数MB程度に抑えるのが扱いやすいです。

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
