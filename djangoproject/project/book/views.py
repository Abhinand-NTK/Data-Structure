from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.


def books(self):
    books = Books.objects.all().prefetch_related('store_set')
    print("------------------")
    print("------------------")
    one = {}
    store = {}
    for i in books:
        one[i.id] = i.name
        store[i.name] = i.store_set.all()
    print(one)
    print(store)
    print(books)
    return HttpResponse("message")