from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'web/index.html')


def register(request):
    return render(request, 'web/register.html')


def search(request):
    return render(request, 'web/search.html')
