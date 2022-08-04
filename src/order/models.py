from book.models import BookCard
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    # Create Cart
    customer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='customer',
    )
    create_date = models.DateField(
        auto_now_add=True,
        help_text='Date first create of Cart',
        blank=True,
        null=True,)
    update_date = models.DateField(
        auto_now=True,
        help_text='Date update of Cart',
        blank=True,
        null=True,)

    def __str__(self):
        return self.name


class BookInCart(models.Model):
    # Create book information in cart
    cart = models.ForeignKey(
        Cart,
        verbose_name='customer',
        on_delete=models.PROTECT)
    book = models.ForeignKey(
        BookCard,
        on_delete=models.PROTECT,
        help_text='Book in Cart',
        verbose_name='Book')
    quantity = models.PositiveSmallIntegerField(
        verbose_name='quantity books in cart',
        default=1,)
    price = models.DecimalField(
        verbose_name='Sum price',
        max_digits=7,
        decimal_places=2,
    )
    create_date = models.DateField(
        auto_now_add=True,
        help_text='Date first add book in Cart',
        blank=True,
        null=True,)
    update_date = models.DateField(
        auto_now=True,
        help_text='Date last update of book in Cart',
        blank=True,
        null=True,)

    def __str__(self):
        return self.name
