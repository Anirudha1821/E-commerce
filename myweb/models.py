from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=60)
    product_desc=models.CharField(max_length=200)
    product_pub_date=models.DateField()

    
    
