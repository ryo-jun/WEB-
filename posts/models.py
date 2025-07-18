from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField("タイトル", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    protagonist = models.CharField("主人公はどんな人？", max_length=100, blank=True)
    setting_detail = models.CharField("舞台の具体的な様子は？", max_length=200, blank=True)
    key_item = models.CharField("物語のキーアイテムは？", max_length=100, blank=True)
    twist = models.TextField("意外な展開やどんでん返しは？", blank=True)
    content = models.TextField("生成された原稿", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("コメント")
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return self.text[:20]
