from django import forms
from django.forms import ModelForm
from .models import *


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ScheduleModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class' : 'form-control form-control-lg'}),
        self.fields['description'].widget.attrs.update({'class' : 'form-control form-control-lg'}),
        self.fields['completed'].widget.attrs.update({'class' : 'form-control form-control-lg'}),
        self.fields['category'].widget.attrs.update({'class' : 'form-control form-control-lg'}),
    
 