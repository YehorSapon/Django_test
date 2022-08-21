from bs4 import BeautifulSoup
from django import template
from django.utils import timezone
import requests


register = template.Library()


@register.simple_tag()
def get_currency():
    """Add currency exchange on page."""

    s = requests.Session()
    r = s.get(
        'https://www.nbrb.by/api/exrates/rates/840?parammode=1').json()

    return r
