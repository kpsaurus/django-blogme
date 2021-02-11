from django.http import HttpResponse
from django.shortcuts import render
from .models import (Post, Tag, Category)


def index(request):
    posts = Post.objects.all()
    if posts:
        return render(request, "pages/posts.html", {"posts": posts})
    else:
        return HttpResponse('No posts found....')


def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "pages/post.html", {"post": post})
    except Post.DoesNotExist:
        return HttpResponse('No post found....')


def tag(request, slug):
    try:
        tag = Tag.objects.get(slug=slug)
    except Tag.DoesNotExist:
        return HttpResponse('No tags found....')
    posts = Post.objects.filter(tag=tag)
    if posts:
        return render(request, "pages/posts.html", {"posts": posts})
    else:
        return HttpResponse('No posts found....')


def category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return HttpResponse('No category found....')
    posts = Post.objects.filter(category=category)
    if posts:
        return render(request, "pages/posts.html", {"posts": posts})
    else:
        return HttpResponse('No posts found....')
