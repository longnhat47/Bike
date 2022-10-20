from django import forms
from bike.models import Bike


class BikeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})
        self.fields['license_plate'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-check-input ml-4'})

    class Meta:
        model = Bike
        fields = ('name', 'type', 'license_plate', 'image', 'status')

