from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Books


@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('title', 'date', 'author', 'genre', 'count_of_pages', 'price',
                    'in_stock', 'review')
