from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.demo= Image(name = 'Demo', decription ='Used to demo a project', location ='Moringa', category='School')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.demo,Image))

   # Testing Save Method
    def test_save_method(self):
        self.demo.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

#Category Class Tests
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.school= Category(name = 'School')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.school,Category))

   # Testing Save Method
    def test_save_method(self):
        self.school.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

#Location Class Tests
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.moringa= Category(name = 'Moringa')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.moringa,Location))

   # Testing Save Method
    def test_save_method(self):
        self.moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


   



