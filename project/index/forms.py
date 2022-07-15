from django.forms import ModelForm
from .models import *


class Base(ModelForm):
    class Meta:
        model = Main
        fields = '__all__'
        exclude = ['img']
