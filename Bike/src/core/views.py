from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bike.models import Type, Bike, Evaluate, CustomUser
# Create your views here.


# @login_required(login_url='login')
def home(request):
    types = Type.objects.all()
    return render(request, 'core/index.html', {'types': types})


def about(request):
    types = Type.objects.all()
    return render(request, 'core/about_us.html', {'types': types})

def adminpage(request):
    types = Type.objects.all()
    bikes = Bike.objects.all()
    customers = CustomUser.objects.all()
    evalutes = Evaluate.objects.all()
    if request.user.is_staff:
        return render(request, 'core/admin.html', {'types': types, 'bikes': bikes, 'customers':  customers, 'evalutes': evalutes})
    else:
        return render(request, 'core/404.html')