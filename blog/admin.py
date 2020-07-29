from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'category', 'author']
    list_filter = ['create_time','category']
    search_fields = ['title']
 

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)