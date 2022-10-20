from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from login.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "last_name",
        "gender",
        "phone",
        "cmnd",
        "birthday",
        "address"
    )

    def gender(self, obj):
        return format_html("Nam" if obj.gender == 0 else "Nữ")




admin.site.register(CustomUser, CustomUserAdmin)