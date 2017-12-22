from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django import forms
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'Post/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Post/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # print(request)
            # post.author = request.user
            post.author = request.GET['id']
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'Post/post_new.html', {'form': form})
    # return render(request, 'Post/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Post/post_edit.html', {'form': form})


def search(request):
    posts = Post.objects.all()
    return render(request, 'search.html', {'posts': posts})
