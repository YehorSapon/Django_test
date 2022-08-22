# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DeleteView, DetailView
from django.urls import reverse_lazy
from book.models import BookCard
from order.models import Cart, BookInCart, Order

# Create your views here.


def get_cart(view):
    # get or create a cart
    cart_id = view.request.session.get('cart')
    if not cart_id:
        if view.request.user.is_anonymous:
            customer = None
        else:
            customer = view.request.user
        cart = Cart.objects.create(
            customer=customer)
        view.request.session['cart'] = cart.pk
    else:
        cart = Cart.objects.get(pk=cart_id)
    return cart


class AddToCart(TemplateView):
    template_name = "order/cart.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        book_id = self.request.GET.get('book_id')
        quantity = int(self.request.GET.get('quantity'))
        # get a cart by get_cart func. See above def get_cart()
        cart = get_cart(self)
        # add book in the cart
        book = BookCard.objects.get(pk=book_id)
        price = quantity * book.price
        # check if the book in the cart exists in DB
        book_in_cart, created = BookInCart.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={
                'quantity': quantity,
                'price': price, })
        if not created:
            # if the book in cart was in the DB - update quantity and price
            book_in_cart.quantity = book_in_cart.quantity + quantity
            book_in_cart.price += book_in_cart.quantity * price
            book_in_cart.save()

        context['cart'] = cart
        context['book_in_cart'] = book_in_cart
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
        books = self.request.GET.keys()
        for prod in books:
            if prod[:5] == 'prod_':  # to get only prod__ key
                book_pk = int(prod.split('__')[1])
                book_update_in_cart = BookInCart.objects.get(pk=book_pk)
                book_update_in_cart.quantity = int(self.request.GET.get(prod))
                book_update_in_cart.price = book_update_in_cart.price * book_update_in_cart.quantity
                book_update_in_cart.save()
            else:
                continue
        # next to check which button onclick
        action_type = self.request.GET.get('action-type')
        if action_type == 'Order':
            Order.objects.create(cart=book_update_in_cart.cart,)
            self.request.session.delete('cart')
        return cart

    def render_to_response(self, context, **kwargs):
        action_type = self.request.GET.get('action-type')
        if action_type == 'Order':
            return HttpResponseRedirect("/")
        return super().render_to_response(context, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
