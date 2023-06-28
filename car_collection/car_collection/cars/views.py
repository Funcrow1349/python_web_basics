from django.shortcuts import render, redirect

from car_collection.cars.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm
from car_collection.cars.models import Car, Profile


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'common/catalogue.html', context)


def car_create(request):
    form = CarCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarEditForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        form = CarDeleteForm(instance=car)
    else:
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-delete.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    cars = Car.objects.all()
    cars_total_price = sum(car.price for car in cars)

    context = {
        'cars': cars,
        'cars_total_price': cars_total_price,
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == "POST":
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')

