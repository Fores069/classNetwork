from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from .forms import PostsForm
from .models import Posts, Category


def home_page(request):
    return render(request,'main/index.html')




def show_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request,'main/post_detail.html',{'post_id': post_id,'post': post})


def show_category(request, cat_slug):
    posts = Posts.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()
    return render(request,'main/category_detail.html',{'posts': posts, 'cat_selected':1})
