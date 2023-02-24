from django.shortcuts import render
from .models import Books
from .resources import BooksResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
import pandas as pd
from django.http import JsonResponse
from django.conf import settings


def home_page(request):
    database = Books.objects.all()
    return render(request, 'database/database_home.html', {'database': database})


def import_data_to_db(request):
    if request.method == 'POST':
        books_resource = BooksResource()
        dataset = Dataset()
        new_books = request.FILES['file']

        if not new_books.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'database/create.html')

        imported_data = dataset.load(new_books.read(), format='xlsx')
        for data in imported_data:
            value = Books(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
                )
            value.save()
    return render(request, 'database/create.html')
