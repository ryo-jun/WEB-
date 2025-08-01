from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment 
from .forms import PostCreationForm, PostFreeForm, CommentForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:home')
    else:
        form = UserCreationForm()
    return render(request, 'posts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('posts:home')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:login')

@login_required
def home(request):
    all_posts = Post.objects.all().order_by('-created_at')
    ranking_posts = Post.objects.all().order_by('-created_at')[:5]
    context = {
        'all_posts': all_posts,
        'ranking_posts': ranking_posts,
    }
    return render(request, 'posts/home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            protagonist = form.cleaned_data['protagonist']
            setting_detail = form.cleaned_data['setting_detail']
            key_item = form.cleaned_data['key_item']
            twist = form.cleaned_data['twist']
            generated_content = f"【{title}】\n\n主人公は「{protagonist}」。\n物語の舞台は「{setting_detail}」。\nそこで重要な役割を果たすのが、キーアイテムの「{key_item}」だ。\n\n物語は順調に進むかと思いきや、最後に「{twist}」という衝撃のどんでん返しが待っていたのだった…！\n\n(この文章はAIの代わりにプログラムが自動生成しました)"
            post.content = generated_content
            post.save() 
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostCreationForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    if request.method == 'POST' and 'comment_submit' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', pk=post.pk)
    context = {
        'post': post,
        'comment_form': comment_form,
        'is_liked': post.likes.filter(id=request.user.id).exists()
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('posts:post_detail', pk=post.pk)

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('posts:home')
    if request.method == 'POST':
        post.delete()
        return redirect('posts:home')
    return render(request, 'posts/delete_post_confirm.html', {'post': post})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    query = request.GET.get('q')
    if query:
        posts = posts.filter(title__icontains=query)
    context = { 'posts': posts, 'query': query, }
    return render(request, 'posts/my_posts.html', context)

@login_required
def select_creation_method(request):
    return render(request, 'posts/select_creation_method.html')

@login_required
def create_post_freely(request):
    if request.method == 'POST':
        form = PostFreeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostFreeForm()
    return render(request, 'posts/create_post_freely.html', {'form': form})
