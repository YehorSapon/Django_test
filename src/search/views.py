from django.shortcuts import render
from django.views import generic
from book import models

# Create your views here.


class SearchList(generic.ListView):
    template_name = "search/search.html"
    model = models.BookCard

    def get_queryset(self, *args, **kwargs):
        if request.method == "POST":
            search = request.method.POST.get('search_q')
            if search != None:
                rs = self.model.objects.filter(name__contains="search")
                return rs
            else:
                return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = request.method.POST.get('search_q')
        return context
