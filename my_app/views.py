from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    #request.POST returns a dictionary, .get accesses the value at 'search'
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)