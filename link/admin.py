from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    list_display = ['name','about','address']
    search_fields = ['name']


admin.site.register(Link, LinkAdmin)