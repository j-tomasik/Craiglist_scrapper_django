from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

BASE_CRAIGSLIST_URL = 'http://sanfrancisco.craigslist.org/search/?query={}'

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    #request.POST returns a dictionary, .get accesses the value at 'search'
    search = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))

    response = requests.get('https://sfbay.craigslist.org/search/sss?query=computer#search=1~gallery~0~0')
    data = response.text
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend) 