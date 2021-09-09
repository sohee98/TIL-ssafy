### 1. Compiled Bootstrap

CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오. 부트스트랩이 적용되기 위해 작성해야 할 코드를 제출하시오.

*  https://getbootstrap.com/docs/5.1/getting-started/download/ 파일 다운로드

* settings.py

  ```
  STATICFILES_DIRS = [
  	BASE_DIR / 'static',
  ]
  ```

* project/static/css/bootstrap.css 파일 추가

* project/static/js/bootstrap.bundle.jss 파일 추가

* base.html

  ```django
  {% load static %}
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <title>Document</title>
  </head>
  <body>
    <div class="container">
      {% block content %}
      {% endblock content %}
    </div>
    <script src="{% static 'js/bootstrap.bundle.js'%}"></script>
  </body>
  </html>
  
  ```

  