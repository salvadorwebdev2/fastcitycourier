from django.db import models



class Sender(models.Model):
    first_name = models.TextField(default='')
    last_name = models.TextField(default='') 
    address = models.TextField(default='')
   
   
class Product(models.Model):
    sender = models.ForeignKey(Sender, default=None, on_delete=models.CASCADE)   
    product_name = models.TextField(default='')    
    product_details = models.TextField(default='')
    product_type = models.TextField(default='')  


class Category(models.Model):
    category_type = models.TextField(default='')
    location = models.TextField(default='')
    time = models.TextField(default='')
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE) 


class Price(models.Model):       
    payment = models.TextField(max_length=50)
    methods = models.TextField(max_length=50)
    services = models.ForeignKey(Category, default=None, on_delete=models.CASCADE) 


class Feedback(models.Model):
    feedback = models.TextField(default='') 
    comment = models.TextField(default='') 
    price = models.ForeignKey(Price, default=None, on_delete=models.CASCADE) 
   
