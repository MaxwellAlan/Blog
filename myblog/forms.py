from django import forms
from .models import Category,Tag,Post


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ('cotegory',)

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name',]

class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields=['name',]

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body']