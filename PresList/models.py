from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
	#1st input
    fullname = models.TextField(default='')
    Owner = models.TextField(default='')

    #2nd
    fname = models.TextField(default='')
    ir = models.TextField(default='')
    bname = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)
