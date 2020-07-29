from django.shortcuts import render
from django.shortcuts import redirect
from .models import Comments
from .forms import CommentsForm
# Create your views here.
def comment(request):
    comments = Comments.objects.all()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/comment')
    else:
        form = CommentsForm()

    return render(request,'comments.html',locals())