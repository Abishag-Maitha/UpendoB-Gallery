from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .form import ImageForm
from .models import Image, Location, Category
from django.contrib import messages

# Create your views here.
def welcome(request):
    all_images=Image.objects.all()
    return render(request, 'index.html', {'images':all_images})


def imageView(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(welcome)
    else:
        form = ImageForm()
    return render(request, 'uploads.html', {'form' : form})
  
def uploadok(request):
    return HttpResponse(' upload successful')

def search_category(request):

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_categories = Image.search_image(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

def view_image(request,id):
    image = Image.objects.filter(id=id).first()
    return render(request, 'image_details.html',{'image':image})

def delete_image(request, id):
    image_deleted=Image.objects.get(id=id)
    image_deleted.delete()
    messages.success(request, 'Image successfully deleted!')
    return redirect(welcome)

def update_image(request, id):
    value=Image.get_image_by_id(id)
    form=ImageForm(request.POST or None, request.FILES or None, instance=value)
    if request.method=='POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'Image updated successfully!')
            return redirect(view_image, id=value.id)
    
    return render (request, 'update.html', {'form':form})

def save_category(request):
    if 'category' in request.POST and request.POST['category']:
        name=request.POST.get('category')
        new_category=Category(name=name)
        new_category.save()
        return redirect(welcome)

def save_location(request):
    if 'location' in request.POST and request.POST['location']:
        name=request.POST.get('location')
        results=Location.objects.filter(name__exact=name).first()
        if results is None:
            new_location=Location(name=name)
            new_location.save()
            return redirect(welcome)