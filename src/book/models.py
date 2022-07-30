"""Create yours models."""

from django.db import models
from django.utils import timezone
from reference.models import Author, PublishingHous, Series_book, Genre_book

COVER = (
    ('1', 'Cardboard'),
    ('2', 'Hardback'),
    ('3', 'Hidebound'),
    ('4', 'Soft'),
)


class BookCard(models.Model):
    """On save, update information about book."""
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='author_book')
    publ_hous = models.ForeignKey(
        PublishingHous,
        on_delete=models.CASCADE,
        related_name='publ_house_book')
    series = models.ForeignKey(
        Series_book,
        on_delete=models.CASCADE,
        related_name='seres_book')
    genre = models.ForeignKey(
        Genre_book,
        on_delete=models.CASCADE,
        related_name='seres_book')
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
        editable=False,
        help_text="Date of create book's card",
        verbose_name="Date add card")
    update_date = models.DateTimeField(
        help_text="Enter publication year",
        verbose_name="Date add book")
    book_cover = models.CharField(
        max_length=20,
        choices=COVER,
        default='soft')


    class Meta:
        ordering = ('-title',)


    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BookCard, self).save(*args, **kwargs)

    def __str__(self):
        """Return self name."""
        return self.title
