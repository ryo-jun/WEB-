from django.contrib import admin
from django.urls import path, include # include をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    # この行を追加
    path('', include('posts.urls')), 
]