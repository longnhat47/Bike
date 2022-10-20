from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from bike.models import Bike, Type
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from bike.forms import BikeForm


# Create your views here.


def rentview(request):
    bikes = Bike.objects.all()
    types = Type.objects.all()
    return render(request, 'core/bike/rentpage.html', {'bikes': bikes, 'types': types})


def rentfilterview(request, *args, **kwargs):
    type_id = kwargs['id']
    bikes = Bike.objects.filter(type__id=type_id)
    types = Type.objects.all()
    return render(request, 'core/bike/filter_bike_page.html', {'bikes': bikes, 'types': types})


@staff_member_required
def adminbikeview(request):
    bikes = Bike.objects.all()

    class Meta:
        ordering = ['name']
    return render(request, 'core/bike/bikes_admin.html', {'bikes': bikes})



class CreateBike(PermissionRequiredMixin, View):
    permission_required = 'login.login'

    def get(self, request):
        form = BikeForm()
        if request.user.is_staff:
            return render(request, 'core/bike/add_bike.html', {'form': form})
        else:
            return render(request, 'core/404.html')


    def post(self, request):
        form = BikeForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            bike = Bike(
                name=form.cleaned_data['name'],
                type=form.cleaned_data['type'],
                license_plate=form.cleaned_data['license_plate'],
                image=form.cleaned_data['image']
            )
            bike.save()

        bikes = Bike.objects.all()
        if request.user.is_staff:
            return render(request, 'core/bike/bikes_admin.html', {'bikes': bikes})
        else:
            return render(request, 'core/404.html')



class EditBike(PermissionRequiredMixin, View):
    permission_required = 'login.login'

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        bike = Bike.objects.get(id=id)
        types = Type.objects.all()
        return render(request, 'core/bike/edit_bike.html', {'bike': bike, 'types': types})


    def post(self, request, *args, **kwargs):
        print(self, request, args, kwargs)
        id = kwargs['pk']
        bike = Bike.objects.get(id=id)
        form = BikeForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data['image'])
            bike.name = form.cleaned_data['name']
            bike.type_name = Type.objects.get(name=form.cleaned_data['type'])
            bike.license_plate = form.cleaned_data['license_plate']
            if form.cleaned_data['image'] != None:
                bike.image = form.cleaned_data['image']
            else:
                bike.image = bike.image
            bike.status = form.cleaned_data['status']
            bike.save()
        bikes = Bike.objects.all()
        if request.user.is_staff:
            return render(request, 'core/bike/bikes_admin.html', {'bikes': bikes})
        else:
            return render(request, 'core/404.html')



class DeleteBike(PermissionRequiredMixin, DeleteView):
    permission_required = 'login.login'
    model = Bike
    template_name = 'core/bike/delete_bike.html'
    success_url = reverse_lazy('bike_admin')
