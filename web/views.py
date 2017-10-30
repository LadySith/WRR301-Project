from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from web.forms import RegisterForm
from web.models import Location, Trip, Route


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
    trips = None
    form_data = None
    route = None
    error_msg = None
    if request.method == 'POST':
        start_location = request.POST.get('start_location', -1)
        end_location = request.POST.get('end_location', -1)

        try:
            start_location_obj = Location.objects.get(id=start_location)
            end_location_obj = Location.objects.get(id=end_location)

            route = Route.objects.get(start_location=start_location_obj, end_location=end_location_obj)

            form_data = [start_location_obj, end_location_obj]

            trips = Trip.objects.filter(route=route)
        except (ValueError, Location.DoesNotExist):
            error_msg = 'Start/End Location not found'
        except Route.DoesNotExist:
            error_msg = 'Route not found'
        except:
            print(start_location)
    return render(request, 'web/search.html',
                  {'trips': trips, 'form_data': form_data, 'route': route, 'error_msg': error_msg})


@login_required
def location_json(request):
    json_output = []
    q = request.GET.get('term', '')
    locations = Location.objects.filter(name__istartswith=q)

    for location in locations:
        data = {
            'value': location.id,
            'label': location.name
        }
        json_output.append(data)

    return JsonResponse(json_output, safe=False)
