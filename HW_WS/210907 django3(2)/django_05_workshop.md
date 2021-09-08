### (1) Read

![image-20210907125017486](md-images/image-20210907125017486.png)

* index.html

```django
{% extends 'base.html' %}

{% block content %}
  
  <h2 class='fw-bold'>Articles</h2>
  <a href="{% url 'articles:create' %}">NEW</a>
  <hr>
  {% for article in articles %}
    <div class='fw-bold fs-2'>{{ article.pk }}</div>
    <div class='fw-bold fs-2'>{{ article.title }}</div>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
  {% endfor %}
{% endblock %}
```



![image-20210907125225261](md-images/image-20210907125225261.png)

* create.html

```django
{% extends 'base.html' %}

{% block content %}
  <h2 class='fw-bold'>New</h2>
  <form action="{% url 'articles:create' %}" method="POST" class='fw-bold'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value='submit' class='fw-bold'>
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock  %}
```





### (3) Detail

![image-20210907124500967](md-images/image-20210907124500967.png)

* detail.html

```django
{% extends 'base.html' %}

{% block content %}
  <h2 class='fw-bold'>DETAIL</h2>
  <hr>
  <h3 class='fw-bold'>글 번호: {{ article.pk }}</h3>
  <h3 class='fw-bold'>글 제목 : {{ article.title }}</h3>
  <p class='fs-5'>글 내용 : {{ article.content }}</p>
  <p>글 생성시각: {{ article.created_at }}</p>
  <p>글 수정시각: {{ article.updated_at }}</p>
  <a href="{% url 'articles:update' article.pk %}">EDIT</a><br>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type='submit' value='DELETE'>
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```





### (4) Update

![image-20210907125115318](md-images/image-20210907125115318.png)

* update.html

```django
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  <h1 class='fw-bold'>EDIT</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" class='fw-bold'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value='submit' class='fw-bold'>
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock  %}
```





### (5) Delete

별도 페이지 없음



### ■ Views.py

```python
from django.shortcuts import get_object_or_404, render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # update
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # edit
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```



### ■ forms.py

```python
from articles.models import Article
from django import forms
   
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'maxlength': 10
            }
        )
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'rows': 10,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
```



