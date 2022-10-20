from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, TemplateView, DeleteView

from bike.models import Bike, Type
from orders.forms import OrderForm
from orders.models import Orders, RentType


# Create your views here.
class RentBikeView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_active == False:
            return redirect('login')
        else:
            form = OrderForm()
            id = kwargs['pk']
            bike = Bike.objects.get(id=id)
            types = Type.objects.all()
            return render(request, 'core/order/rentbike.html', {'form': form, 'bike': bike, 'types': types})

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            id = kwargs['pk']
            bike = Bike.objects.get(id=id)
            user = request.user
            rent_day_start = int(form.cleaned_data['rent_day_start'].strftime('%Y%m%d'))
            rent_day_end = int(form.cleaned_data['rent_day_end'].strftime('%Y%m%d'))
            day = rent_day_end - rent_day_start
            if day == 0:
                day = 1
            if day > 30:
                type_rent = RentType.objects.get(name='Tháng')
            elif day > 7:
                type_rent = RentType.objects.get(name='Tuần')
            else:
                type_rent = RentType.objects.get(name='Ngày')

            price = bike.type.price * day * type_rent.price / 100

            order = Orders(
                bike=bike,
                customer=user,
                rent_day_start=form.cleaned_data['rent_day_start'],
                rent_day_end=form.cleaned_data['rent_day_end'],
                type_rent=type_rent,
                price=price,
                status=False
            )
            order.save()

            bike.status = False

            bike.save()
            id = request.user.id
            orders = Orders.objects.filter(customer__pk=id)
        return render(request, 'core/index.html', {'orders': orders})



class RentListView(View):
    def get(self, request):
        id = request.user.id
        orders = Orders.objects.filter(customer__pk=id)
        types = Type.objects.all()
        return render(request, 'core/order/list_order.html', {'orders': orders, 'types': types})


class OrderListView(View):
    def get(self, request):
        orders = Orders.objects.all()
        return render(request, 'core/order/order_admin.html', {'orders': orders})


class OrderDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        order = Orders.objects.get(id=id)
        return render(request, 'core/order/order_detail.html', {'order': order})

    def post(self, request, *args, **kwargs):
        print(self, args, kwargs, request)
        id = kwargs['id']
        order = Orders.objects.get(id=id)
        order.status = True
        order.save()
        orders = Orders.objects.all()
        return render(request, 'core/order/order_admin.html', {'orders': orders})


class DeleteOrder(PermissionRequiredMixin, DeleteView):
    permission_required = 'login.login'
    model = Orders
    template_name = 'core/order/delete_order.html'
    success_url = reverse_lazy('order-admin')
    def post(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs['pk'])
        bike = order.bike
        bike.status = True
        bike.save()
        order.delete()
        orders = Orders.objects.all()
        return render(request, 'core/order/order_admin.html', {'orders': orders})
