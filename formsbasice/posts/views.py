from django.db.models import Q
from django.shortcuts import render, redirect

from posts.forms import PostBaseForm, PostCreateForm, PostEditForm, PostDeleteForm, SearchForm
from posts.models import Post


# Create your views here.
def index(request):
    # For example
    # form = MyForm(request.POST or None)
    # if request.method == "GET":
    #     form = MyForm()
    # else:
    #     form = MyForm(request.POST)
    # if request.method == 'POST' or form.is_valid():
    #     print(form.cleaned_data.get("my_text"))
    # form = PostForm(request.POST or None)
    # if request.method == 'POST' and form.is_valid():
    #     form.save()
    # context = {'form': form}
    return render(request, 'index.html')


def dashboard(request):
    posts = Post.objects.all()
    search_form = SearchForm(request.GET)
    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data['query']
        posts = Post.objects.filter(
            Q(title__icontains=query)
            |
            Q(content__icontains=query)
            |
            Q(author__icontains=query)
        )
    context = {
        'posts': posts,
        'search_form': search_form,

    }
    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(request.POST or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'posts/edit-post.html', context)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)
    # if request.method == 'POST' and post.is_valid():
    #     post.save()
    #     return redirect('dashboard')
    context = {
        'post': post,
    }
    return render(request, 'posts/post-details.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'posts/delete-post.html', context)