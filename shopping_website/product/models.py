from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey("self", on_delete = models.CASCADE, db_constraint=False, null=True)

class Product(models.Model):
    name= models.CharField(max_length= 100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE) 
    description = models.TextField()
    img_path = models.TextField(default="")
    price =models.FloatField()
    is_active=models.BooleanField(default=False)
    quantity=models.FloatField()



#many to one relation between product and category


