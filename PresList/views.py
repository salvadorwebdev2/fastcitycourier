from django.shortcuts import render, redirect
from django.http import HttpResponse
from PresList.models import Item, List


def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})
    


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'registration.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(Owner =request.POST['on'],fname =request.POST['od'], list=list_)
    return redirect(f'/PresList/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    #para sa 1st item ng 2nd html
    Item.objects.create(fullname=request.POST['fname'],ir =request.POST['ir'],bname =request.POST['bname'],list=list_)
    return redirect(f'/PresList/{list_.id}/')




