from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField('昵称',max_length=100)
    email = models.EmailField('邮箱')
    text = models.TextField('评论内容')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])