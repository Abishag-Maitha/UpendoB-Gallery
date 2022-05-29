from django.db import models

   
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(category=value)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    @classmethod
    def update_category(cls,id,value):
        cls.objects.filter(id=id).update(category=value)

class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads')
    name = models.CharField(max_length =50)
    description = models.TextField(max_length =1000, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)
   

    @classmethod
    def search_image(cls,category):
        images=cls.objects.filter(category__name__icontains=category).all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.filter(id=id).first()
        return image

    @classmethod
    def filter_by_location(cls,location):
        image_location=Image.objects.filter(location__name=location).all()
        return image_location