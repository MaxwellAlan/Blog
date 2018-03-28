from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Tag
import markdown
from .forms import SigninForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# Create your views here.
def blog(request):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    post_list = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'post_list': post_list, 'tag_list': tag_list, 'category_list': category_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def signin(request):
    if request.method == "POST":
        signin_form=SigninForm(request._post)
        if signin_form.is_valid():
            cd=signin_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("Welcome.")
            else:
                return HttpResponse("Sorry.")
        else:
            return HttpResponse("Invalid signin")
    if request.method == "GET":
        signin_form=SigninForm()
        return render(request, 'signin.html',context={'form':signin_form})
