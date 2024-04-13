from django import forms
from .models import Reservation
import datetime
from datetime import timedelta

class ReservationForm(forms.Form):
    start_date = forms.DateField(required=True,label='Fecha de inicio',widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}))
    end_date = forms.DateField(required=True,label='Fecha de fin',widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}))

    def __init__(self, *args, **kwargs):
        self.book = kwargs.pop('book', None)  
        super(ReservationForm, self).__init__(*args, **kwargs)

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        if start_date < datetime.date.today():
            raise forms.ValidationError("La fecha de inicio no puede ser en el pasado.")
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        if end_date < datetime.date.today():
            raise forms.ValidationError("La fecha de fin no puede ser en el pasado.")
        if 'start_date' in self.cleaned_data:
            start_date = self.cleaned_data['start_date']
            if end_date < start_date:
                raise forms.ValidationError("La fecha de fin no puede ser antes de la fecha de inicio.")
            if end_date == start_date:
                raise forms.ValidationError("La fecha de fin no puede ser igual a la fecha de inicio.")
            if end_date > start_date:
                difference = end_date - start_date
                if difference <= timedelta(days=6):
                    raise forms.ValidationError("La diferencia entre la fecha de inicio y la fecha de fin debe ser de más de 6 días.")
                elif difference >= timedelta(days=30):
                    raise forms.ValidationError("La diferencia entre la fecha de inicio y la fecha de fin debe ser de menos de un mes.")
        existing_reservations = Reservation.objects.filter(book=self.book, end_date__gte=start_date, start_date__lte=end_date)
        if len(existing_reservations) > 0:
            raise forms.ValidationError("El libro no está disponible en las fechas seleccionadas.")
        return end_date