from django.shortcuts import render, redirect
from django.http import HttpResponse
from PresList.models import Sender, Product, Category, Price, Feedback


def home_page(request):
    senders = Sender.objects.all()
    return render(request, 'homepage.html',{'senders' : senders})


def view_list(request, sender_id):
    sender_= Sender.objects.get(id=sender_id)
    return render(request, 'registration.html', {'sender': sender_})


def new_list(request):
    sender_= Sender.objects.create()
    #product.objects.create(Owner =request.POST['on'],fname =request.POST['od'], Sender=Sender)
    return redirect(f'/PresList/{sender_.id}/')

def add_item(request, sender_id):
    sender_ = Sender.objects.get(id=sender_id)
 
    #product.objects.create(fullname=request.POST['fname'],ir =request.POST['ir'],bname =request.POST['bname'],Sender=Sender)
    return redirect(f'/PresList/{sender_.id}/')


def dataManipulation(request):
    #Creating data
    people = Sender(first_name="Ding", last_name="Manuel", address="bkl66 lt66 GreenGate" )
    people.save()

    #Read all data
    courier = Sender.objects.all()
    result = 'Printing all customers list : <br>'
    for x in courier:
        res += X.first_name+"<br>"

    #Read one data
    box = Sender.get(id="19")
    res += "Printing one customer profile : <br>"
    res += box.last_name

    #Delete data
    res+= '<br> Deletinng... <br>'
    box.delete()

    #Update data
    people = Sender.objects.get(first_name="Ding")
    people.product_name = "Packs of Briefs"
    people.save()
    res = ""

    #Filtering data
    qs = Booking.objects.filter(first_name="Ding")
    res += "found : %s result<br>"%len(qs)

    #ordering data
    qs = Sender.objects.order_by("first_name")
    for x in qs: 
        res += x.first_name + x.last_name + '<br>'



