from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Burgerking
from .forms import BurgerkingForm

# Create your views here.
def index(request):
    return render(request, 'burgerking/index.html')

def menu(request):
    burgers = Burgerking.objects.order_by('pk')
    context = {
        'burgers': burgers,
    }
    return render(request, 'burgerking/menu.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BurgerkingForm(request.POST, request.FILES)
        if form.is_valid():
            burger = form.save()
            return redirect('burgerking:detail', burger.pk)
    else:
        form = BurgerkingForm()
    context = {
        'form': form,
    }
    return render(request, 'burgerking/create.html', context)

@require_safe
def detail(request, pk):
    burger = get_object_or_404(Burgerking, pk=pk)
    context = {
        'burger': burger,
    }
    return render(request, 'burgerking/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    burger = get_object_or_404(Burgerking, pk=pk)
    if request.method == 'POST':
        form = BurgerkingForm(request.POST, request.FILES, instance=burger)
        if form.is_valid():
            form.save()
            return redirect('burgerking:detail', burger.pk)
    else:
        form = BurgerkingForm(instance=burger)
    context = {
        'burger': burger,
        'form': form,
    }
    return render(request, 'burgerking/update.html', context)

@require_POST
def delete(request, pk):
    burger = get_object_or_404(Burgerking, pk=pk)
    burger.delete()
    return redirect('burgerking:menu')
