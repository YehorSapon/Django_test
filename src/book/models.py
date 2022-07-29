from django.db import models

# Create your models here.


class BookCard(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="Enter book title",
        verbose_name="Book title")
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        help_text="Enter price in BYN",
        verbose_name="Book price",
        null=True,
        blank=True)
    publ_year = models.DateField(
        auto_now=False,
        help_text="Enter publication year",
        verbose_name="Year of publication",
        null=True,
        blank=True)
    pages = models.SmallIntegerField(
        default=1,
        help_text="Enter amount pages",
        verbose_name="Pages",
        null=True,
        blank=True)
    wieght = models.IntegerField(
        help_text="Enter weight in g",
        verbose_name="Weight",
        null=True,
        blank=True)
    available_books = models.SmallIntegerField(
        default=1,
        help_text="Enter amount available books",
        verbose_name="Amount available books",
        null=True,
        blank=True)
    is_available = models.BooleanField(
        default=False,
        verbose_name="Available for order",
        null=True,
        blank=True)
    add_date = models.DateField(
        auto_now_add=False,
        help_text="Date of create book's card",
        verbose_name="Date add card")
    last_change_date = models.DateField(
        auto_now_add=True,
        auto_created=True,
        help_text="Enter publication year",
        verbose_name="Date add book")

    def __str__(self):
        return self.title
