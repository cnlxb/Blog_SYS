from django.contrib import admin
from .models import *
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name','about','url','create_time']
    search_fields = ['name']

admin.site.register(Link,LinkAdmin)