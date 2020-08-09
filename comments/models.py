from django.db import models
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    name = models.CharField('姓名', max_length=50)
    email = models.EmailField('个人邮箱')
    text = models.TextField('留言内容')
    create_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])