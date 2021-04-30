from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	#if request.method == 'POST':
		#return HttpResponse(request.POST['blk'])
	#return render(request,'homepage.html',{'permit':request.POST['permit'],'pin':request.POST['pin'],})
	return render(request,'homepage.html',{'blk':request.POST.get('blk',''),'bn' :request.POST.get('bn',''),'rn' :request.POST.get('rn','')})
