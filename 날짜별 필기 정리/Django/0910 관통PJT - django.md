* From의 역할 2가지
  * data validation 유효성 검사
  * HTML(`<input>`) 생성



* 띄어쓰기
  * `<p>{{ question.content|linebreaksbr }}</p>`



* category

  ```python
  # models.py
  CATEGORY_CHOICES = [
  	('python', '파이썬'),
      ('실제 저장되는 값', '사용자가 보게 될 값'),
  ]
  
  class Question(models.Model):
  	category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
  ```

  ```django
  # detail.html
  {{ question.get_category_display }}
  ```

  > `instance.get_[field]_display`



* Forms.py

  ```python
  class QuestionForm(models.ModelForm):
  	title = forms.CharField(
      	min_length=2,
          max_length=100,
          required=True
      )
  ```

  * model의 필드와 이름이 같다면,  DB에 저장이 된다.

  * model의 필드가 아니면, HTML+검증은 하되 저장은 하지 않는다.

    

* checkbox

  ```python
  # forms.py
  is_save = forms.BooleanField(required=False, label='wanna save?', help_text='저장하려면 체크하세요')
  
  class Meta:
      model Question
      # 아래 필드는 모델에 있어야 하며, 데이터검증 + HTML생성을 합니다
      fields = ('title', 'category', 'content')
      # exclude = ('field_a')
  ```

  ```python
  def create(request):
      if request.method == 'POST':
          form = QuestionForm(request.POST)
          if form.is_valid():
          	if form.cleaned_data['is_save']:
                  question = form.save()
                  return redirect('board:detail', question.pk)
              else:
                  return redirect('board:create')
      else:
          form = QuestionForm()
      context = {
          'form': form,
      }
      return render(request, 'board/create.html', context)
  ```



* bootstrap 적용

  ```python
  # setttings.py
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [BASE_DIR / 'static'] # 추가로 탐색
  ```

  ```django
  # base.html
  {% load bootstrap5 %}
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'board/css/custom.css' %}">
  ...
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
  ```

  > /static/css/bootstrap.min.css
  >
  > /static/css/bootstrap.min.css.map
  >
  > /static/css/bootstrap.min.js
  >
  > /static/css/bootstrap.min.js.map

  > custion css : board/static/css/custom.css



* include

  * templates/_navbar.html 생성 (`_`는 구분하기 위해서)

  ```django
  # base.html
  {% include '_navbar.html' %}
  ```



* Paginator

  ```python
  def index(request):
      questions = Question.get.object.order_by('-pk')
      paginator = Paginator(questions, 3) #Show 25 contacts per page
      page_number = request.Get.get('page')
      page_obj = paginator.get_page(page_number)
      
      context = { 
      	'page_obj': page_obj,
      }
      return render(request, 'board/create.html', context)
  ```

  ```django
  # index.html
  {% load bootstrap5 %}
  
  <ul>
    {% for question in page_obj %}
    <li>
        <a href="{% url 'board:detail' question.pk %}">{{ question.title }}</a>
    </li>
    {% end for %}
  </ul>
  <div class='d-flex justify-content-center'>
    {% bootstrap_pagination page_obj %}
  </div>
  ```



* form

  ```django
  # form.html
  <form method="Post">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button>제출</button>
  </form>
  ```

  













