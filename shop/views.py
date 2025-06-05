from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    nSlides=n//4+ceil(n/4-n//4)
    allProds=[[products,range(1,len(products)),nSlides],[products,range(1,len(products)),nSlides]]
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('We are at contact.')

def tracker(request):
    return HttpResponse('We are at tracker.')

def search(request):
    return HttpResponse('We are at search.')

def productview(request):
    return HttpResponse('We are at productview.')

def checkout(request):
    return HttpResponse('We are at checkout.')