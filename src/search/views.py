from django.shortcuts import render
from django.views import generic
from book import models

# Create your views here.


def search_books(request):
    if request.method == 'POST':
        search = request.POST['search_q']
        results = models.BookCard.objects.filter(title__contains=search)
        return render(request,
                      'search/search.html',
                      {'search': search,
                       'results': results})
    else:
        return render(request, 'search/search.html', {})
