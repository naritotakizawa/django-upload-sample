# django-upload-sample
ファイルアップロードをする幾つかの方法についてを説明しています。

* 単一ファイルのアップロード

    * モデルを利用しない
    * モデルを利用する

* 複数ファイルのアップロード

    * フォームセット(モデルなし)
    * モデルフォームセット(モデルあり)
    * input multiple(モデルなし)
    * input multiple(モデルあり)
    
[ブログ記事](https://blog.narito.ninja/detail/92)


## 動かし方
```bash
git clone https://github.com/naritotakizawa/django-upload-sample
cd django-upload-sample
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```
