from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # Review
    ## CRUD
    path('create/', views.create_review, name='create_review'),
    path('', views.review_index, name='review_index'),
    path('<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/update/', views.update_review, name='update_review'),
    path('<int:review_pk>/delete/', views.delete_review, name='delete_review'),
    
    ## Like & Dislike
    path('<int:review_pk>/like/', views.like_review, name='like_review'),
    path('<int:review_pk>/dislike/', views.dislike_review, name='dislike_review'),

    # Comment
    ## CD
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
