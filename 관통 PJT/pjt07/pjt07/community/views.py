from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg

from .models import Review, Comment
from .forms import ReviewForm, CommentForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm()

    context = {'form': form, }
    return render(request, 'community/review/create.html', context)


@require_safe
def review_index(request):
    # reviews = Review.objects.all()     
    rank_avg = Review.objects.aggregate(Avg('rank'))
    reviews = Review.objects\
                .annotate(comment_count=Count('comment'))\
                .select_related('user')

    context = {
        'reviews': reviews,
        'rank_avg': rank_avg['rank__avg'],
    }
    return render(request, 'community/review/index.html', context)


@require_safe
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'review': review,  
        'form':form,
    }
    return render(request, 'community/review/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
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
    if request.user == review.user:
        review.delete()
    return redirect('community:review_index')


@login_required
@require_POST
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('community:review_detail', review.pk)


@login_required
@require_POST
def dislike_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.dislike_users.filter(pk=request.user.pk).exists():
        review.dislike_users.remove(request.user)
    else:
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
            comment.user = request.user
            comment.save()
        return redirect('community:review_detail', review.pk)


@login_required
@require_POST
def delete_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('community:detail', review.pk)
