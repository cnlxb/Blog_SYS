from django.contrib import admin
from .models import Comments
# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','email','create_time']
    search_fields = ['name']

admin.site.register(Comments,CommentsAdmin)