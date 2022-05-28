from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .form import ImageForm
from .models import Image, Location, Category

# Create your views here.
def welcome(request):
    all_images=Image.objects.all()
    return render(request, 'index.html', {'images':all_images})


def imageView(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'uploads.html', {'form' : form})
  
def uploadok(request):
    return HttpResponse(' upload successful')

