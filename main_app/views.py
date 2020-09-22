from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Addon, Photo
from .forms import MaintenanceForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'carcollector-69'

@login_required
def addons_index(request):
    addons = Addon.objects.all()
    return render(request, 'addons/index.html', {'addons': addons})

@login_required
def addons_detail(request, addon_id):
    addon = Addon.objects.get(id=addon_id)
    return render(request, 'addons/detail.html', {'addon': addon})

class AddonCreate(LoginRequiredMixin, CreateView):
    model = Addon
    fields = '__all__'  

class AddonUpdate(LoginRequiredMixin, UpdateView):
    model = Addon
    # We can choose what the user can Update
    fields = ['name', 'color']

class AddonDelete(LoginRequiredMixin, DeleteView):
    model = Addon
    success_url = '/addons/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)

def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    maintenance_form = MaintenanceForm()
    addons_car_doesnt_have = Addon.objects.exclude(id__in=car.addons.all().values_list('id'))
    return render(request, 'cars/detail.html', { 
        'car': car,
        'maintenance_form': maintenance_form,
        'addons': addons_car_doesnt_have
         }) 

@login_required
def assoc_addon(request, car_id, addon_id):
    Car.objects.get(id=car_id).addons.add(addon_id)
    return redirect('detail', car_id=car_id)

@login_required
def unassoc_addon(request, car_id, addon_id ):
    Car.objects.get(id=car_id).addons.remove(addon_id)
    return redirect('detail', car_id=car_id)


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = [  'make', 'model', 'color',  'vin', 'year' ]  
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'

@login_required
def add_maint(request, car_id):
    form = MaintenanceForm(request.POST)

    if form.is_valid():
        new_maint = form.save(commit=False)
        new_maint.car_id = car_id
        new_maint.save()
    return redirect('detail', car_id=car_id)

@login_required
def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except Exception as e:
            print('An error occurred uploading file to s3')
            print(e)
    return redirect('detail', car_id=car_id)

