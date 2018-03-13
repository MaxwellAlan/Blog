from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import markdown
from django.utils.html import strip_tags
# Create your models here.

# 分类
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


#标签
class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


#博客
class Post(models.Model):
    #文章标题
    title=models.CharField(max_length=100,verbose_name="标题")
    #文章内容
    body=models.TextField(verbose_name="博客内容")
    #发表时间
    created_time=models.DateTimeField(default=timezone.now,verbose_name="发表时间")
    #修改时间
    modified_time=models.DateTimeField(verbose_name="最后修改时间")
    #摘要
    excerpt=models.CharField(max_length=200,blank=True,verbose_name="摘要")
    #分类
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类")
    #标签
    tages=models.ManyToManyField(Tag,blank=True,verbose_name="标签")
    #作者
    author=models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE,verbose_name="作者")
    # 阅读量
    view_times = models.PositiveIntegerField(default=0)

    class Meta:
        ordering=("-created_time",)

    def increase_view_times(self):
        self.views += 1
        self.save(update_fields=['view_times'])

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)
