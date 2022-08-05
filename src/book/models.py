"""Create yours models."""

from django import forms
from django.db import models
from django.utils import timezone
from reference.models import Author, PublishingHous, Series_book, Genre_book

COVER = (
    ('1', 'Cardboard'),
    ('2', 'Hardback'),
    ('3', 'Hidebound'),
    ('4', 'Soft'),
)
AGE = (
    ('1', '0+'),
    ('2', '6+'),
    ('3', '12+'),
    ('4', '16+'),
    ('5', '18+'),
)
FORMAT_BOOK = (
    ('1', 'Foolscap octavo'),
    ('2', 'Crown octavo'),
    ('3', 'Demy octavo'),
    ('4', 'Royal octavo '),
)


class BookCard(models.Model):
    """On save, update information about book."""

    author = models.ManyToManyField(
        Author,
        related_name='author_book')
    publ_hous = models.ManyToManyField(
        PublishingHous,
        related_name='publ_house_book',
        null=True,
        blank=True)
    series = models.ManyToManyField(
        Series_book,
        related_name='seres_book',
        null=True,
        blank=True)
    genre = models.ManyToManyField(
        Genre_book,
        related_name='genre_book',
        null=True,
        blank=True)
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
    picture = models.ImageField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name="Pictire of book",
        null=True,
        blank=True)
    pages = models.SmallIntegerField(
        default=1,
        help_text="Enter amount pages",
        verbose_name="Pages",
        null=True,
        blank=True)
    weight = models.IntegerField(
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
    create_date = models.DateTimeField(
        editable=True,
        auto_now_add=True,
        help_text="Date of create book's card",
        verbose_name="Date add card",
        name="Date of create book card")
    update_date = models.DateTimeField(
        help_text="Enter publication year",
        auto_now=True,
        verbose_name="Date add book")
    book_cover = models.CharField(
        verbose_name="Book cover",
        max_length=10,
        choices=COVER,
        default='4',
        null=True,
        blank=True)
    age_restrictions = models.CharField(
        verbose_name="Age restrictions of book",
        max_length=5,
        choices=AGE,
        default='1',
        null=True,
        blank=True)
    book_format = models.CharField(
        verbose_name="Book format",
        name="format",
        max_length=5,
        choices=FORMAT_BOOK,
        default='1',
        null=True,
        blank=True)

    class Meta:
        ordering = ['-title']

    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BookCard, self).save(*args, **kwargs)

    def __str__(self):
        """Return self name."""
        return self.title
