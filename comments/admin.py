from django.contrib import admin
from .models import *

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_time']
    fields = ['name', 'email', 'text',]


admin.site.register(Comment, CommentAdmin)