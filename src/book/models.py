"""Create yours models."""

from django.db import models
from django.utils import timezone
from django.urls import reverse
from reference.models import Author, PublishingHous, Series_book, Genre_book

COVER = (
    ('Cardboard', 'Cardboard'),
    ('Hardback', 'Hardback'),
    ('Hidebound', 'Hidebound'),
    ('Soft', 'Soft'),
)
AGE = (
    ('0+', '0+'),
    ('6+', '6+'),
    ('12+', '12+'),
    ('16+', '16+'),
    ('18+', '18+'),
)
FORMAT_BOOK = (
    ('Foolscap octavo', 'Foolscap octavo'),
    ('Crown octavo', 'Crown octavo'),
    ('Demy octavo', 'Demy octavo'),
    ('Royal octavo', 'Royal octavo'),
)


class BookCard(models.Model):
    """On save, update information about book."""

    author = models.ManyToManyField(
        Author,
        related_name='author_book')
    publ_hous = models.ForeignKey(
        PublishingHous,
        related_name='publ_house_book',
        on_delete=models.PROTECT,
        null=True,
        blank=True)
    series = models.ManyToManyField(
        Series_book,
        related_name='seres_book',
        blank=True)
    genre = models.ManyToManyField(
        Genre_book,
        related_name='genre_book',
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
        default=1.00,
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
        default=1,
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
        verbose_name="Date add card on site",
        name="Date of create book card")
    update_date = models.DateTimeField(
        help_text="Enter publication year",
        auto_now=True,
        verbose_name="Date add book")
    book_cover = models.CharField(
        verbose_name="Book cover",
        max_length=10,
        choices=COVER,
        default='Soft',
        null=True,
        blank=True)
    age_restrictions = models.CharField(
        verbose_name="Age restrictions of book",
        max_length=5,
        choices=AGE,
        default='0+',
        null=True,
        blank=True)
    book_format = models.CharField(
        verbose_name="Book format",
        name="format",
        max_length=20,
        choices=FORMAT_BOOK,
        default='Royal octavo',
        null=True,
        blank=True)

    class Meta:
        ordering = ['Date of create book card']

    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BookCard, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': self.pk},
                       current_app='book')

    def display_authors(self):
        """Create a string for the Author. This is required to display author if they more then one."""
        return ', '.join(author.surname for author in self.author.all()[:5])
    display_authors.short_description = 'Authors'

    def display_genres(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genres.short_description = 'Genres'

    def display_series(self):
        return ', '.join(series.name for series in self.series.all()[:3])
    display_series.short_description = 'Series'

    def __str__(self):
        """Return instance BookCard name."""
        return self.title
