from django.contrib import admin
from PresList.models import Sender, Product, Category, Price, Feedback
# Register your models here.
admin.site.register(Sender)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Feedback)