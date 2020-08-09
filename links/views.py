from django.shortcuts import render
from .models import *
# Create your views here.
def link(request):
    link_list = Link.objects.all()
    return render(request,'links.html',locals())