from django.contrib import admin
from reference import models

# Register your models here.


admin.site.register(models.PublishingHous)
admin.site.register(models.Genre_book)
admin.site.register(models.Series_book)


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'second_name', 'surname', 'date_birth', 'date_death')
    list_filter = ('name', 'surname')
    search_fields = ('name', 'surname')
