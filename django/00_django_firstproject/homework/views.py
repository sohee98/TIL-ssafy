from django.shortcuts import render

# Create your views here.
def hw(request):
    menus = ['음식1', '음식2']
    posts = ['0번째', '1번째', '2번째']
    users = []
    context = {
        'menus' : menus,
        'posts' : posts,
        'users' : users,
    }
    return render(request, 'hw.html', context)

