from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Prefetch

from .models import Review, Comment
from .forms import ReviewForm, CommentForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm()

    context = {'form': form, }
    return render(request, 'community/review/form.html', context)


@require_safe
def review_index(request):
    
    """
    DOCUMENT: https://docs.djangoproject.com/en/3.2/ref/models/querysets/
    
    # aggregate => 압축하다.
    # 리뷰들의 평점평균 구하기 (returns dict)
    rank_avg = Review.objects.aggregate(Avg('rank'))
    
    # annotate => 추가로 기록하다
    # 리뷰 데이터에 관련 댓글 개수를 comment_count 필드에 추가로 기록하여 불러오기
    reviews = Review.objects.annotate(comment_count=Count('comment'))

    # select_realted (정참조) => N이 FK 가 있는 1의 정보를 합쳐서 불러오기
    reviews = Review.objects.select_related('author')

    # prefetch_related (역참조) => 1이 N에 대한 / M:N 상황에서 역참조 정보를 불러오기
    reviews = Review.objects.prefetch_related('comment_set')
    
    """
    # 단순 리뷰데이터 전체
    # reviews = Review.objects.all()    
    
    rank_avg = Review.objects.aggregate(Avg('rank'))

    reviews = Review.objects\
                .annotate(comment_count=Count('comment'))\
                .select_related('author')

    context = {
        'reviews': reviews,
        'rank_avg': rank_avg['rank__avg'],
    }
    return render(request, 'community/review/index.html', context)


@require_safe
def review_detail(request, review_pk):
    """
    # Review =역참조=> Comment =정참조=> User
    reviews = Review.objects.prefetch_related(
        Prefetch(
            'comment_set',
            queryset=Comment.objects.select_related('author')
        )
    )
    """

    # queryset 생성
    queryset = Review.objects\
                .annotate(
                    # like_users 를 카운트하여 필드에 추가
                    like_count=Count('like_users'),
                    # dislike_users 를 카운트하여 필드에 추가
                    dislike_count=Count('dislike_users')
                )\
                .select_related('author')\
                .prefetch_related(
                    Prefetch(
                        'comment_set',
                        queryset=Comment.objects.select_related('author')
                    )
                )

    # queryset 에서 단일 객체 찾기
    review = get_object_or_404(queryset, pk=review_pk)
    
    form = CommentForm()
    context = {
        'review': review,
        'form': form,    
    }
    return render(request, 'community/review/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.author:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save()
                return redirect('community:review_detail', review.pk)
        else:
            form = ReviewForm(instance=review)

        context = {'form': form, }
        return render(request, 'community/review/form.html', context)
    else:
        return redirect('community:review_detail', review.pk)


@login_required
@require_POST
def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.author:
        review.delete()
    return redirect('community:review_index')


@login_required
@require_POST
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 이미 좋아요를 했다면,
    # if request.user in review.like_users.all():
    if review.like_users.filter(pk=request.user.pk).exists():
        # 취소
        review.like_users.remove(request.user)
    # 아니라면
    else:
        # 추가
        review.like_users.add(request.user)
    return redirect('community:review_detail', review.pk)


@login_required
@require_POST
def dislike_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.dislike_users.filter(pk=request.user.pk).exists():
        # 취소
        review.dislike_users.remove(request.user)
    # 아니라면
    else:
        # 추가
        review.dislike_users.add(request.user)
    return redirect('community:review_detail', review.pk)


@require_POST
def create_comment(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.save()
        return redirect('community:review_detail', review.pk)


@login_required
@require_POST
def delete_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('community:detail', review.pk)
