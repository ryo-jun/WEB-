from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # ログイン後のホームページ
    path('home/', views.home, name='home'),
    
    # ログイン、ログアウト、サインアップ
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # 原稿作成と詳細表示
    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # 削除機能
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),

    # 自分の投稿一覧・検索機能
    path('my-posts/', views.my_posts, name='my_posts'),

    # 投稿方法の選択機能
    path('select-method/', views.select_creation_method, name='select_method'),
    path('create-freely/', views.create_post_freely, name='create_freely'),
    
    # いいね機能
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]