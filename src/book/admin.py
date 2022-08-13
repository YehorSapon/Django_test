from django.contrib import admin
from book import models

# Register your models here.


@admin.register(models.BookCard)
class BookCardAdmin(admin.ModelAdmin):
    """Registration and representation of the model BookCard in the admin interface."""

    list_display = ('title', 'publ_hous', 'display_authors',
                    'display_series', 'display_genres', 'publ_year',
                    )
    fields = ['title', 'author', 'series',
              'genre', ('publ_hous', 'price', 'publ_year',
                                 'available_books',)]
    list_filter = ('title', 'author', 'publ_hous',
                   'series', 'genre',)
    search_fields = ('title', 'author', 'publ_hous',
                     'series', 'genre',)
