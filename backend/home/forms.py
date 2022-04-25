from django import forms
from django.forms import ModelForm

from .models.reserve import ReserveHome


class ReserveHomeForm(ModelForm):
    res_entry_date = forms.CharField(max_length=50, help_text='Введите дату приезда')
    res_depart_date = forms.CharField(max_length=50, help_text='Введите дату отъезда')
    res_adult = forms.IntegerField(help_text='Введите количество взрослых')
    res_child = forms.IntegerField(help_text='Введите количество детей')
    res_created_at = forms.DateTimeField(help_text='Введите текущую дату')

    class Meta:
        model = ReserveHome
        fields = ['res_entry_date',
                  'res_depart_date',
                  'res_adult',
                  'res_child']

