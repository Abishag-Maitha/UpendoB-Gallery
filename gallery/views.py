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

def search_images(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.objects.search_image(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

