from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect,HttpResponse

from .forms import *
from .models import *
# Create your views here.
def comment(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('comment'))
    else:
        form = CommentForm()
    
    return render(request,'comments.html',locals())
