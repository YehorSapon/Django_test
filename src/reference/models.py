from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        max_length=25,
        help_text="Enter author name",
        verbose_name="Author's name")
    second_name = models.CharField(
        max_length=25,
        help_text="Enter author name",
        null=True,
        blank=True)
    surname = models.CharField(
        max_length=25,
        help_text="Enter author surname",
        verbose_name="Author's surname")
    date_birth = models.DateField(
        help_text="Enter author's birth year",
        blank=True,
        null=True,)
    date_death = models.DateField(
        help_text="Enter author's year of death",
        blank=True,
        null=True,)

    def __str__(self):
        return self.surname


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

    def __str__(self):
        return self.name
