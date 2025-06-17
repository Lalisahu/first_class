from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact

def app(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def About(request):
    return render(request, 'About.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        
    return render(request, 'contact.html')
def Services(request):
    return render(request, 'Services.html')

# Create your views here.
