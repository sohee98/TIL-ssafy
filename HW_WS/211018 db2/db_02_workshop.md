### ❖ Django Model Relationship - 댓글 기능 구현하기



* models.py

  ```python
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.TextField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.content
  ```



* forms.py

  ```python
  from django import forms
  from .models import Comment
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ('article',)
  ```



* urls.py

  ```python
  from django.urls import path
  from . import views
  
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/delete/', views.delete, name='delete'),
      path('<int:pk>/update/', views.update, name='update'),
      path('<int:pk>/comments/', views.comments_create, name='comments_create'),
      path('<int:article_pk>/comments/<int:comment_pk>/delete/', 
  			views.comments_delete, name='comments_delete')
  ]
  ```

  

* detail.html

  ````html
  <!-- 댓글 목록 -->
    <h4>댓글 목록</h4>
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}"
                method = "POST" class='d-inline'>
            {% csrf_token %}
            <input type="submit" value='DELETE'>      
          </form>      
        </li>
      {% endfor %}
    </ul>
    <hr>
  
  <!-- 댓글 작성 form -->
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  ````

  

* views.py

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from .forms import CommentForm
  
  def detail(request, pk):
      article = get_object_or_404(Article, pk=pk)
      comment_form = CommentForm()            # 댓글 작성
      comments = article.comment_set.all()    # 댓글 출력
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
  
  def comments_create(request, pk):
      article = get_object_or_404(Article, pk=pk)
      comments_form = CommentForm(request.POST)
      if comments_form.is_valid():
          comment = comments_form.save(commit=False)
          comment.article = article
          comment.save()
      return redirect('articles:detail', article.pk)
  
  def comments_delete(request, article_pk, comment_pk):
      comment = get_object_or_404(CommentForm, pk=comment_pk)
      comment.delete()
      return redirect('articles:detail', article_pk)
  ```

  