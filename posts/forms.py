from django import forms
from .models import Post, Comment

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'protagonist', 'setting_detail', 'key_item', 'twist']

class PostFreeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = { 'content': forms.Textarea(attrs={'rows': 15, 'placeholder': 'ここに自由に話の原稿を書いてください...'}), }
        labels = { 'title': 'タイトル', 'content': '原稿', }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = { 'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'コメントを追加...'}), }
        labels = { 'text': '', }
