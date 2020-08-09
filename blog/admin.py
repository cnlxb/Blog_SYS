from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'category', 'author']
    list_filter = ['create_time','category']
    search_fields = ['title']
 

admin.site.register(Post, PostAdmin)
admin.site.register(Category)


#修改网页title和站点header。
admin.site.site_title = "后台管理"
admin.site.site_header = "刘小备_Blog"
