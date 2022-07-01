from django.shortcuts import render

from .models import *


def Mirjon(request):
    base = MainId.objects.all()
    return render(request, 'base.html', {'ombor': base})

