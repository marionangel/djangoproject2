from django.shortcuts import render


def Home(request):
    return render(request,'index.html' )

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Services(request):
    return render(request, 'service.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Product(request):
    return render(request, 'product.html')