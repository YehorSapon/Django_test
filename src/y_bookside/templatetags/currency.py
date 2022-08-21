from bs4 import BeautifulSoup
from django import template
from django.utils import timezone
import requests


register = template.Library()


@register.simple_tag()
def get_currency():
    """Add currency exchange on page."""

    start = timezone.now()
    s = requests.Session()
    r = s.get(
        'https://www.nbrb.by/')
    soup = BeautifulSoup(r.content, 'html.parser')
    finish = timezone.now()
    delta = finish - start
    return r
