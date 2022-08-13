from django.contrib import admin
from reference import models

# Register your models here.


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    """Registration and representation of the model Author in the admin interface."""

    list_display = ('name', 'second_name', 'surname',
                    'date_birth', 'date_death')
    list_filter = ('name', 'surname')
    search_fields = ('name', 'surname')


@admin.register(models.PublishingHous)
class PublishingHousAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(models.Genre_book)
class Genre_bookAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(models.Series_book)
class Series_bookAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
