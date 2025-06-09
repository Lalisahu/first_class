from django.shortcuts import render,HttpResponse

def app(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def About(request):
    return render(request, 'About.html')
def Contact(request):
    return render(request, 'Contact.html')
def Services(request):
    return render(request, 'Services.html')

# Create your views here.
