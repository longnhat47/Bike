from django import forms

from orders.models import Orders
from bike.models import Bike
from login.models import CustomUser


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rent_day_start'].widget.attrs.update({'class': 'form-control day_picker'})
        self.fields['rent_day_end'].widget.attrs.update({'class': 'form-control day_picker'})

    class Meta:
        model = Orders
        widgets = {
            'rent_day_start': DatePickerInput(),
            'rent_day_end': DatePickerInput()
        }
        fields = ('rent_day_start', 'rent_day_end')

