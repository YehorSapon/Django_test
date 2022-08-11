from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, DetailView
from django.urls import reverse_lazy
from book.models import BookCard
from order.models import Cart, BookInCart

# Create your views here.


def get_cart(view):
    cart_id = view.request.session.get('cart')
    if not cart_id:
        if view.request.user.is_anonymous:
            customer = None
        else:
            customer = view.request.user
        cart = Cart.objects.create(
            customer=customer
        )
        view.request.session['cart'] = cart.pk
    else:
        cart = Cart.objects.get(pk=cart_id)
    return cart


class AddToCart(TemplateView):
    template_name = "order/cart.html"

    def get_context_data(self, **kwargs):
        book_id = self.request.GET.get('book_id')

        # get a cart
        cart = get_cart(self)
        # add book in the cart
        if book_id:
            book = BookCard.objects.get(pk=book_id)
            quantity = int(self.request.GET.get('quantity'))
            price = BookCard.objects.get(pk=book_id).price * quantity
            # check if the book in the cart exists in DB
            book_in_cart, created = BookInCart.objects.get_or_create(
                cart=cart,
                book=book,
                defaults={
                    'quantity': quantity,
                    'price': price, })
            if not created:
                # if the book in cart was in the DB - update quantity and price
                book_in_cart.quantity += quantity
                book_in_cart.price += book_in_cart.quantity * price
                book_in_cart.save()

        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        return context


class DeleteFromCart(DeleteView):
    template_name = "order/item_del.html"
    model = BookInCart
    success_url = reverse_lazy('order:add-in-cart')


class UpdateCart(DetailView):
    template_name = "order/cart.html"
    model = BookInCart

    def get_object(self, **kwargs):
        cart = get_cart(self)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
