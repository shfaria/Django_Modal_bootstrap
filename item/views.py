from django.shortcuts import render, redirect
from .form import *

def home(request):
    return render(request, 'item/home.html')

def edit(request):
    if request.method == "POST":
        form = simple(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = simple()
    return render(request, 'item/edit.html', {
        'form': form,
    })

