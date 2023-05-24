# devcontainer_sample
devcontainerを設定した時の初期状態

## プレーンパターン手順 (devcontainer_plane)
1. VS Codeでコマンドパレットから `Add Dev Container Configuration Files` を選択する
2. コンテナのテンプレートを選択する。`Python 3`など。
3. Pythonのバージョンを選択する。`3.11`など。
4. 必要な追加機能を選択する、ここでは選択せずにOKする
5. Reopen in Containerする

## Dockerfileを使ってみる (devcontainer_dockerfile)
1. Dockerfileを追加する
2. devcontainer.jsonのimageタグを削除
3. `"dockerFile" : "Dockerfile"` を追加する
4. Dockerfileのaptを最新化して、必要なライブラリをインストールするコマンドを書く
5. DockerfileにDevContainer内のユーザーを作るコマンドを書く
6. devtontainer.jsonのcustomizationsを記述する
    * vscode -> extensions にextension IDを指定する
    * vscode -> settings にVSCodeの設定を指定する
7. runArgsに.envファイルを渡すようにする
   * ⚠️ .envファイルがない場合コンテナの起動がエラーになります
8. remoteUserにユーザーを指定する
9.  コマンドパレットから Rebuild Containerする

## Poetryのパッケージ管理手順 (devcontainer_poetry)

1. poetryの初期設定を行って、pyproject.tomlを生成する
```
$ poetry init
```

2. パッケージを追加する (ここではpytest)

```
$ poetry add pandas
$ poetry add pytest -dev  # 開発環境用
```

3. パッケージをインストールする

```
$ poetry install            # 全部インストール
$ poetry install --no-dev   # 開発環境用をインストールしない
```
4. Dev Container上でpoetryでinstallする

devcontainer.jsonにpoetry installを追加する
```
"postCreateCommand": "poetry install",
```

## Docker-Composeでデータベースを一緒に起動する (devcontainer_docker-compose)

1. docker-compose.ymlを追加する
   1.  .devcontainer_docker-compose/docker-compose.yml 参照
   2.  devcontainer.jsonのrunArgsが使えないので、docker-composeで.envを取り込むようにする
```
      env_file:
      - .env
```
2. initdb.dディレクトリを追加して、SQLファイルを格納する
     * docker-entrypoint-initdb.d 内のファイルがコンテナ作成時に実行されるらしい
3. devcontainer.jsonの記述を追加します
```
	"dockerComposeFile": "docker-compose.yml",
	"service": "main",
```

1. ビルドしなおして、DBにアクセスできるか確認します。


## 参考情報

* devcontainer.jsonのリファレンス
  * https://containers.dev/implementors/json_reference/
