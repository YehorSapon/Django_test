# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import models
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DeleteView
from django.views.generic import DetailView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from book.models import BookCard
from order.models import Cart, BookInCart, Order
from order import forms


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
    model = Cart
    success_url = reverse_lazy("order:add-to-cart")

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
            if self.request.user.is_anonymous:
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(reverse_lazy("user_app:profile"))
        return super().render_to_response(context, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OrdersList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "order/order_list.html"
    model = Order
    permission_required = 'order.view_order'
    login_url = reverse_lazy("user_app:login")

class OrderView(LoginRequiredMixin, DetailView):
    template_name = "order/order.html"
    model = Order
    login_url = reverse_lazy("user_app:login")


class OrderEdit(LoginRequiredMixin, UpdateView):
    template_name = "order/order_edit.html"
    model = Order
    form_class = forms.OrderEditForm
    login_url = reverse_lazy("user_app:login")
    # success_url = "/reference/author/list/"


class OrderDelete(LoginRequiredMixin, DeleteView):
    template_name = "reference/order_del.html"
    model = Order
    login_url = reverse_lazy("user_app:login")
    # success_url = "/"
