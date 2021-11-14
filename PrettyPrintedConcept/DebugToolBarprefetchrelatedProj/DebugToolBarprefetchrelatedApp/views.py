from django.shortcuts import render
from .models import Store,Book
# Create your views here.
def index_view(request):
    #now we want to fetch all the Stores Having the Books
    books-Book.objects.prefetch_related('store_set').all()
    for book in books:
        stores=book.store_set.all()
    return None
