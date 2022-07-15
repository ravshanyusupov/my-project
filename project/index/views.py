from django.shortcuts import render, redirect
from .models import *
from .forms import Base


def Mirjon(request):
    base = Main.objects.all()
    return render(request, 'base.html', {'base': base})


def second(request, kalit):
    base = Main.objects.get(id=kalit)
    return render(request, 'second.html', {'base1': base})


def create(request):
    form = Base()
    if request.method == 'POST':
        form = Base(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', {'form': form})


def update(request, id):
    user = Main.objects.get(id=id)
    form = Base(instance=user)
    if request.method == 'POST':
        form = Base(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(f'/sec/{id}')
    return render(request, 'create.html', {'form': form})


def delete(request, id):
    user = Main.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    return render(request, 'delete.html', {'user': user})





