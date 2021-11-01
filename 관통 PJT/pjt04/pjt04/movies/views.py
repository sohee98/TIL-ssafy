from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request): 		# 전체 영화 목록 조회 
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):    # 단일 영화 상세 조회
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)


## Create
def new(request):		# 사용자가 데이터를 제출할 빈 html 제공
    return render(request, 'movies/new.html')

def create(request):		# 사용자가 데이터를 제출한 데이터를 새로운 movie에 저장
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.overview = request.POST.get('overview')
    movie.poster_path = request.POST.get('poster_path')
    movie.save()
    return redirect('movies:index')	    #새로고침, 영화목록조회페이지로 


## Update
def edit(request, pk):		# 데이터를 제출할 기준 내용이 있는 html 제공
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):	# 사용자가 제출한 데이터를 '기존 movie'에 저장
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.overview = request.POST.get('overview')
    movie.poster_path = request.POST.get('poster_path')
    movie.save()
    return redirect('movies:detail', movie.pk)


## Delete - 기존 movie을 삭제
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        
        return redirect('movies:index')
    else:
        return redirect('movies:detail', pk)

