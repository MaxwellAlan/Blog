from django import forms
from .models import Category


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ('cotegory',)

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)