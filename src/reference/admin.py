from django.contrib import admin
from reference import models

# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.PublishingHous)
admin.site.register(models.Genre_book)
admin.site.register(models.Series_book)
