from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AddToCart(TemplateView):
    template_name = "order/cart.html"

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        return context
