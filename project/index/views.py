from django.shortcuts import render

from .models import *


def Mirjon(request):
    base = Main.objects.all()
    a = [
        {'name': 'Ravshan', 'age': 20, 'number': 9898998},
        {'name': 'Ravshan', 'age': 20, 'number': 9898998}
    ]
    return render(request, 'base.html', {'ombor': base, 'print': a})

