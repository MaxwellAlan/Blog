from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题")
    body=models.TextField(verbose_name="博客内容")
    created_time=models.DateTimeField(default=timezone.now,verbose_name="发表时间")
    modified_time=models.DateTimeField(verbose_name="最后修改时间")
    excerpt=models.CharField(max_length=200,blank=True,verbose_name="摘要")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类")
    tages=models.ManyToManyField(Tag,blank=True,verbose_name="标签")
    author=models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE,verbose_name="作者")

    class Meta:
        ordering=("-created_time",)

    def __str__(self):
        return self.title