from django.test import TestCase

# Create your tests here.
from .models import Product

class ModelTest(TestCase):

    def testProductModel(self):
        product = Product.objects.create(name="ToyCar", price=800)
        self.assertEquals(str(product), 'ToyCar')
        print("IsInstance : ",isinstance(product,Product))
        self.assertTrue(isinstance(product,Product))

    