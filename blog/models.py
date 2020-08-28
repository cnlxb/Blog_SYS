from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 文章分类
class Category(models.Model):
    name = models.CharField('文章分类',max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name
  
 # 博客文章
class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    picture = models.ImageField('图片', upload_to='pictures/', blank=True)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    about = models.TextField('文章摘要',max_length=200)
    body = models.TextField('文章正文')  
    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    views = models.PositiveIntegerField('阅读量',default=0, editable=False)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])