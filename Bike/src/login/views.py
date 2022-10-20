from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from login.forms import ProfileForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView

# Create your views here.
from login.models import CustomUser


class LoginClass(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'core/login/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        print(user_name)
        password = request.POST.get('password')
        print(password)
        is_login = authenticate(username=user_name, password=password)
        if is_login is None:
            messages.error(request, 'Your login information is incorrect')
            return redirect('login')

        login(request, is_login)
        if request.user.is_staff:
            return redirect('adminpage')
        else:
            return redirect('home')


def req_logout(request):
    logout(request)
    return redirect('login')


class RegisterClass(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'core/login/register.html')

    def post(self, request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        re_pass = request.POST.get('re_pass')

        if user_name == '':
            messages.add_message(request, messages.ERROR, message='Username cannot be empty')
        if re_pass != password:
            messages.add_message(request, messages.ERROR, message='Repeat password must be the same as the password')
        if len(password) < 8:
            messages.add_message(request, messages.ERROR, message='Password must be more than 8 characters')
        if len(messages.get_messages(request)) > 0:
            return redirect('register')

        user = CustomUser.objects.create_user(user_name, '', password)
        user.save()
        return redirect('login')


class UpdateProfileClass(View):
    def get(self, request, *args, **kwargs):
        print(request)
        id = request.user.id
        user = CustomUser.objects.get(id=id)
        return render(request, 'core/login/update_profile.html', {'user': user})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        male = request.POST.get('gender')
        if male:
            gender = True
        else:
            gender = False
        phone = request.POST.get('phone')
        cmnd = request.POST.get('cmnd')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')

        if first_name == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập họ của bạn')
        if last_name == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập tên của bạn')
        if phone == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập số điện thoại của bạn')
        if cmnd == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập chứng minh nhân dân của bạn')
        if birthday == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập ngày sinh của bạn')
        if address == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập địa chỉ của bạn')
        if len(messages.get_messages(request)) > 0:
            return redirect('update_profile')

        id = request.user.id
        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.gender = gender
        user.phone = phone
        user.cmnd = cmnd
        user.birthday = birthday
        user.address = address
        user.save()
        return redirect('home')


class UserListView(View):

    def get(self, request):
        if request.user.is_authenticated:
            users = get_user_model().objects.all()
            return render(request, 'core/login/user_admin.html', {'users': users})
        return HttpResponseNotFound('<h1>Page not found</h1>')


class UserDetailView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        user = get_user_model().objects.get(id=id)
        return render(request, 'core/login/user_detail.html', {'user': user})

    def post(self, request, *args, **kwargs):
        print(self, args, kwargs, request)
        id = kwargs['id']
        user = get_user_model().objects.get(id=id)
        user.is_staff = True
        user.save()
        users = get_user_model().objects.all()
        return render(request, 'core/login/user_admin.html', {'users': users})


class EditUserClass(View):
    def get(self, request, *args, **kwargs):
        print(self, request, args, kwargs)
        id = kwargs['id']
        user = CustomUser.objects.get(id=id)
        return render(request, 'core/login/edit_user.html', {'user': user})

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        male = request.POST.get('gender')
        if male:
            gender = True
        else:
            gender = False
        phone = request.POST.get('phone')
        cmnd = request.POST.get('cmnd')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')

        if first_name == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập họ của bạn')
        if last_name == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập tên của bạn')
        if phone == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập số điện thoại của bạn')
        if cmnd == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập chứng minh nhân dân của bạn')
        if birthday == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập ngày sinh của bạn')
        if address == '':
            messages.add_message(request, messages.ERROR, message='Hãy nhập địa chỉ của bạn')
        if len(messages.get_messages(request)) > 0:
            return redirect('edit-user-admin')

        id = kwargs['id']
        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.gender = gender
        user.phone = phone
        user.cmnd = cmnd
        user.birthday = birthday
        user.address = address
        user.save()
        return redirect('user-admin')