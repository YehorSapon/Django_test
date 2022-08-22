from book.models import BookCard
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Cart(models.Model):
    # Create Cart
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Customer',
        # By 'usercarts' we can see how many cart users have.
        # Quantities Cart in User
        related_name='usercarts',
        blank=True,
        null=True,)
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

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        return f'{self.customer.get_username(self)} cart {self.pk}'

    @property
    def total_price(self):
        total = 0
        for book_in in self.products_in.all():
            total += book_in.price
        return total


class BookInCart(models.Model):
    # Create book information in cart
    cart = models.ForeignKey(
        'order.Cart',
        verbose_name='Cart',
        on_delete=models.PROTECT,
        # By 'products_in' we can see how many books in cart.
        # Quantities BookInCart in Cart
        related_name='products_in',)
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

    class Meta:
        ordering = ('-create_date',)
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.book.title}#{self.pk}'


class Order(models.Model):
    cart = models.ForeignKey(
        'order.Cart',
        verbose_name='Cart',
        on_delete=models.PROTECT,
        related_name='orders',)
    status = models.ForeignKey(
        'order.OrderStatus',
        verbose_name='Order status',
        on_delete=models.PROTECT,
        related_name='statuses',
        blank=True,
        null=True)
    create_date = models.DateField(
        auto_now_add=True,
        auto_now=False,
        help_text='Date first add book in Cart',
        blank=True,
        null=True)
    update_date = models.DateField(
        auto_now=True,
        auto_now_add=False,
        help_text='Date last update of book in Cart',
        blank=True,
        null=True)
    address = models.CharField(
        max_length=250,
        verbose_name='Adress',
        blank=True,
        null=True)
    paid = models.BooleanField(
        default=False,
        blank=True,
        null=True)

    class Meta:
        ordering = ('-create_date',)
        verbose_name_plural = 'Orders'

    def get_absolute_url(self):
        return reverse('order', kwargs={'pk': self.pk},
                       current_app='order')

    def __str__(self):
        return f'Order {self.cart.custumer} #'


class OrderStatus(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="Enter title oorder status",
        verbose_name="Title order status",
        blank=True,
        null=True)
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True)

    def __str__(self):
        return self.title
