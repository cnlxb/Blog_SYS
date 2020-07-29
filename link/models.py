from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField('友链名称',max_length=100)
    picture = models.ImageField('友链头像',upload_to='static/link_pictures',blank=True)
    about = models.CharField('友链介绍',max_length=128)
    address = models.URLField('友链地址')

    class Meta:
        verbose_name = '链接'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
