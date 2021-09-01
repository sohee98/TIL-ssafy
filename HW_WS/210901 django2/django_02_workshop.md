(1) Read

![image-20210901161954961](md-images/image-20210901161954961.png)

```django
{% extends 'base.html' %}

{% block content %}
  <h1 class="fw-bold">INDEX</h1>
  <a href={% url 'articles:new' %}>NEW</a>
  <br></br>
  <h2>제목: 게시글 제목</h2>
  <p>내용: 게시글 내용</p>
  <a href="{% url 'articles:new' %}">DETAIL</a>
{% endblock %}
```

(2) Create

![image-20210901163427169](md-images/image-20210901163427169.png)

```django
{% extends 'base.html' %}

{% block content %}
  <h1 class="fw-bold">NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    <label for="title">TITLE: </label>
    <input type="text" name="title" id="title"><br>
    <label for "content">CONTENT: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
    <input type="submit" value="작성">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```

