from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('select-method/', views.select_creation_method, name='select_method'),
    path('create-freely/', views.create_post_freely, name='create_freely'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]