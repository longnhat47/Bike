from django import forms
from login.models import CustomUser


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['cmnd'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthday'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'gender', 'phone', 'cmnd', 'birthday', 'address')

