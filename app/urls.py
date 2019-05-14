from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # ファイルの一覧ページ
    path('', views.FileListView.as_view(), name='file_list'),

    # 通常のフォーム
    path('single/upload/', views.SingleUploadView.as_view(), name='single_upload'),

    # モデルフォーム
    path('single/upload/model/', views.SingleUploadWithModelView.as_view(), name='single_upload_with_model'),

    # 複数ファイルを通常フォーム
    path('multi/upload/', views.MultiUploadView.as_view(), name='multi_upload'),

    # 複数ファイル、モデルフォーム
    path('multi/upload/model/', views.multi_upload_with_model, name='multi_upload_with_model'),

    # input multiple
    path('input/multiple/upload/', views.InputMultiUploadView.as_view(), name='input_multi'),
]
