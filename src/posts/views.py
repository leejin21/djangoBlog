from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        "post_list": posts
    }
    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def post_create(request):
    # TODO: 아래 세 줄의 의미 찾기
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        # end the function and call httpresponseRedirect, so that we can go back to the root.
        return HttpResponseRedirect('/posts')
    context = {
        "form": form,
        'form_type': 'Create'
    }

    return render(request, "post_create.html", context)


def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    # 여기서 instance의 의미는?
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context = {
        "form": form,
        'form_type': 'update'
    }
    return render(request, "post_create.html", context)


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/posts')
