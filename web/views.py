from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from web.forms import RegisterForm


def index(request):
    if request.user.is_authenticated:
        return redirect('search')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('search')
    return render(request, 'web/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            # Log in
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('search')
    else:
        form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})


@login_required
def search(request):
    return render(request, 'web/search.html')
