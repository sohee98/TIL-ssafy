from django.shortcuts import render

# Create your views here.
def dinner(request, menu, count):
    context = {
        'menu': menu,
        'count': count,
    }
    return render(request, 'dinner.html', context)