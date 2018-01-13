from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Post/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Post/post_detail.html', {'post': post})


def post_new(request):
    isPostedStr = ""
    isPosted = False

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            if request.FILES['image']:
                post.image = request.FILES['image']
            posts = Post.objects.filter(author=post.author)
            for package in posts:
                if package.package_name == post.package_name:
                    isPostedStr = "The package you are trying to save is already existing!"
                    break
            if isPostedStr == "":
                post.save()
                isPosted = True
    else:
        form = PostForm()
    return render(request, 'Post/post_new.html', {'form': form, 'isPosted' : isPosted, 'isPostedStr' : isPostedStr})


def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('Post/post_detail', id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'Post/post_edit.html', {'form': form, 'id':post.pk})


def search(request):
    posts = Post.objects.all()
    if request.method == "GET":
        businessName = request.GET.get('businessName', "")
        category = request.GET.get('category', 'Wedding')
        print('GET businessName : {}\nGET category : {}' .format(businessName, category))

        noOfBusinesses = 1
        if businessName != "":
            businesses = User.objects.filter(username__contains=businessName)
            for business in businesses:
                print('Business ID #: {}' .format(business.pk))
                noOfBusinesses += 1
            print('No of biz : {}' .format(noOfBusinesses))
            print('\nPosts: {}' .format(posts))
            bizIndex = 0
            for business in businesses:
                if bizIndex == 0:
                    posts = list(Post.objects.filter(author=business.pk).filter(category__contains=category))
                    print('\nIndex number: {}, the first post {}'.format(bizIndex, posts))
                else:
                    posts.append(Post.objects.filter(author=business.pk).filter(category__contains=category))
                    print('\nIndex number: {}, iyang mga posts: {}' .format(bizIndex, posts))
                bizIndex+=1
        else:
            posts = list(Post.objects.filter(category__contains=category))
    print("Rendering the requested template ... {}" .format(posts))
    return render(request, 'Post/search.html', {'posts' : posts})


