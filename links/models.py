from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField('名称',max_length=100)
    avatar = models.ImageField('头像',upload_to='static/avatar',blank=True)
    about = models.CharField('介绍',max_length=200)
    url = models.URLField('地址')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name = '链接'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name