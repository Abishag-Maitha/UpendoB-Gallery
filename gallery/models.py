from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads')
    name = models.CharField(max_length =50)
    description = models.TextField(max_length =200, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    def search_image(category):
        category.search_image()
    



class Location(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)