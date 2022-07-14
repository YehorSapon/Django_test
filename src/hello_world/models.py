from django.db import models

# Create your models here.
class PublishingHous(models.Model):
    name = models.CharField(
        verbose_name="Publishing Hous's name",
        max_length=50,
        )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
        )