from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def  index(request):
	if request.method == "POST":
		email= request.POST.get('email')
		phone= request.POST.get('phone')
		desc= request.POST.get('desc')
		contact=Contact( email=email,phone=phone, desc=desc, date= datetime.today())
		contact.save()

	return render(request,"index.html")


