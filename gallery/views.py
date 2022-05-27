from django.shortcuts import render, redirect
from django.http  import HttpResponse
from gallery.form import ImageForm

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the PendoB Gallery')


def imageView(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'uploads.html', {'form' : form})
  
  
def uploadok(request):
    return HttpResponse(' upload successful')

