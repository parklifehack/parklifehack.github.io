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
├── handwriting/
├── books/
├── beats/
│   ├── volume-1/
│   ├── volume-2/
│   └── volume-3/
├── audio/
│   ├── beat-tape-volume-1/
│   ├── beat-tape-volume-2/
│   └── beat-tape-volume-3/
└── README.md
```

## 写真を置く

最初の写真は、`images/main.jpg` として置いています。

写真を差し替えるときは、新しい画像を同じ名前で置き換えます。

## トピック

トップページには現在、以下をリンクしています。

* `Photos` → `/photos/`
* `Handwriting` → `/handwriting/`
* `Beats` → `/beats/`

`bread/`、`photos/`、`books/` のページは、ストックができたときに再利用できるよう残しています。

## 手書きスキャンを追加する

手書きスキャンは `/handwriting/` に置きます。
画像は1枚で横幅を使い、縦に並べて読めるようにしています。

公開用画像は以下に置きます。

```text
images/handwriting/scan-2026-08-28-1.jpg
```

`handwriting/index.html` の `.handwriting-stack` 内に、同じ形の
`<figure class="handwriting-sheet">` を追加します。

## ビートテープに曲を追加する

ビートテープ用のページは以下です。

* `Vol. 1` → `/beats/volume-1/`
* `Vol. 2` → `/beats/volume-2/`
* `Vol. 3` → `/beats/volume-3/`

`beats/index.html` の一覧は、新しいVolumeが上に来る順番にします。

音源ファイルは以下に置きます。

* Volume 1: `audio/beat-tape-volume-1/`
* Volume 2: `audio/beat-tape-volume-2/`
* Volume 3: `audio/beat-tape-volume-3/`

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

## アクセス確認

GitHub Pages単体ではWebサーバーの生ログやページ別の詳細アクセス解析は取れません。手元から確認できる範囲として、GitHubのTraffic APIでRepo単位の直近14日分のviews/clones、popular paths、referrersを確認します。

```bash
GITHUB_TOKEN=... python3 tools/github_traffic.py
```

このAPIは書き込み権限のあるRepoで使うものです。細かいページ別・地域別・端末別まで見たい場合は、Cloudflare Web Analytics、Plausible、GoatCounterなどの外部アクセス解析をサイトに埋め込む必要があります。

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
