* base.html
* settings
* urls



1. CRUD - articles 

   * admin
   * models
   * forms
   * urls, views, html
     * create - create, detail
     * read - index
     * update
     * delete

   ```python
   from django.views.decorators.http import require_POST, require_http_methods, require_safe
   from django.contrib.auth.decorators import login_required
   
   ```

   



2. forms

   * error

     ```django
       <form action="{% url 'articles:create' %}" method="POST">
         {% csrf_token %}
         {% for field in form %}
           {{ field.errors }}
           {{ field.label_tag }}
           {{ field }}
         {% endfor %}
         <button>작성</button>
       </form>
     ```

     

   

3. Auth - accounts

   * forms

     ```python
     from django.contrib.auth.forms import UserChangeForm
     from django.contrib.auth import get_user_model
     
     class CustomUserChangeForm(UserChangeForm):
     
         class Meta:
             model = get_user_model()
             fields = ('email', 'first_name', 'last_name')
     ```

     

   * urls, views, html
     * login
     * logout
     * signup
     * delete
     * update
     * password

   ```python
   from django.contrib.auth.forms import (
       AuthenticationForm, UserCreationForm, PasswordChangeForm
   )
   from django.contrib.auth import login as auth_login
   from django.contrib.auth import logout as auth_logout
   from django.contrib.auth import update_session_auth_hash
   from .forms import CustomUserChangeForm
   
   
   #login
   form = AuthenticationForm(request, request.POST)
   if form.is_valid():
       auth_login(request, form.get_user())
       return redirect(request.GET.get('next') or 'articles:index')
   
   #signup
   form = UserCreationForm(request.POST)
   if form.is_valid():
       user = form.save()
       auth_login(request, user)  
       return redirect('articles:index')
   
   #update
   form = CustomUserChangeForm(request.POST, instance=request.user)
   if form.is_valid():
       form.save()
       return redirect('articles:index')
           
   #change_password
   form = PasswordChangeForm(request.user, request.POST)
   if form.is_valid():
       form.save()
       update_session_auth_hash(request, form.user)
       return redirect('articles:index')
   
   ```

   

4. Static

   * settings

     ```python
     STATIC_URL = '/static/'
     STATICFILES_DIRS = [
         BASE_DIR / 'static',
     ]
     
     MEDIA_ROOT = BASE_DIR / 'media'
     MEDIA_URL = '/media/'
     ```

     ```
     $ pip install Pillow
     ```

   * models

     ```python
     # articles/models.py
     class Article(models.Model):
         ...
         image = models.ImageField(blank=True, upload_to='images/')
     ```

     > media/images 에 저장됨
     >
     > media 폴더 만듬

   * urls

     ```python
     # articles/urls.py
     from django.conf import settings
     from django.conf.urls.static import static
     
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('articles/', include('articles.urls')),
         path('accounts/', include('accounts.urls'))
     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     ```

   * views

     ```python
     # create
     form = ArticleForm(request.POST, request.FILES)
     
     # update
     form = ArticleForm(request.POST, request.FILES, instance=article)
     ```

   * html

     ```django
     # create.html
     <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit" value="작성" accept="image/*, .pdf">
     </form>
     ```

     ```django
     # detail.html
     {% load static %}
     ...
     # articles/static/articles/
     <img src="{% static 'articles/img2.png' %}" alt="sample image"> 
     # static/images/
     <img src="{% static 'images/img3.png' %}" alt="">
     
     {% if article.image %}
       <img src="{{ article.image.url }}" alt="{{ article.image }}">
     {% endif %}
     ```

     ```django
     # articles/update.html
     <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
     ```

     

