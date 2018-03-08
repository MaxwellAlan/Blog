from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/index.html')


def signin(request):
    return render(request, 'signin.html')
