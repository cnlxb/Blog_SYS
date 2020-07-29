from django.shortcuts import render
from .models import Link
# Create your views here.

def link(request):
    links = Link.objects.all()
    return render(request,'link.html',locals())