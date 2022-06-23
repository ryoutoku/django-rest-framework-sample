# django-rest-framework-sample

django REST framework のサンプルコード集。

以下方針にて作成。

- トリッキーなコードは書かない
- 基本的に必要になるであろう機能を実装
  - jwt による authorization
  - query request による filter
  - camel - snake 変換
- DRY、KISS、YAGNI を意識する
  - class base で作成

## 実行

## 構成

## テスト

### Dockerfile

- [hadolint](https://github.com/hadolint/hadolint)
- [dockle](https://github.com/goodwithtech/dockle)

```bash
# Dockerfileに対するlint
hadolint Dockerfile

# DockerImageに対するセキュリティ等確認
# pip module用にsettings.pyは除外
docker build . -t test
dockle -af settings.py test
```
