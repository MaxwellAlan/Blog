from django.shortcuts import render
from .models import Category, Post, Tag
# Create your views here.
def blog(request):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    post_list = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'post_list': post_list, 'tag_list': tag_list, 'category_list': category_list})


def signin(request):
    return render(request, 'signin.html')
