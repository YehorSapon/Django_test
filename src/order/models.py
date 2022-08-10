from book.models import BookCard
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    # Create Cart
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Customer',
        related_name='usercarts', # By 'usercarts' we can see how many cart users have. Quantities Cart in User
        blank=True,
        null=True,
    )
    create_date = models.DateField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Created order date',
        help_text='Date first create of Cart',
        blank=True,
        null=True,)
    update_date = models.DateField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Updated order date',
        help_text='Date update of Cart',
        blank=True,
        null=True,)

    def total_price(self):
        print(self.products_in.all())
        total = 0
        for book_in in self.products_in.all():
            total += book_in.price
        return total




class BookInCart(models.Model):
    # Create book information in cart
    cart = models.ForeignKey(
        'order.Cart',
        verbose_name='Books in Cart',
        on_delete=models.PROTECT,
        related_name='products_in', # By 'products_in' we can see how many books in cart. Quantities BookInCart in Cart
        )
    book = models.ForeignKey(
        BookCard,
        on_delete=models.PROTECT,
        help_text='Book in Cart',
        verbose_name='Book',
        related_name='books_in',)
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Quantity books in cart',
        default=1,)
    price = models.DecimalField(
        verbose_name='Sum price',
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,)
    create_date = models.DateField(
        auto_now_add=True,
        auto_now=False,
        help_text='Date first add book in Cart',
        blank=True,
        null=True,)
    update_date = models.DateField(
        auto_now=True,
        auto_now_add=False,
        help_text='Date last update of book in Cart',
        blank=True,
        null=True,)


