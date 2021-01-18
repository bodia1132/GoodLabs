# Lab_3: Вступ до моніторингу.

+ Створюємо директорію для лабораторної роботи і ініціалізуємо середовище pipenv та пакети django.
```
pipenv --python 3.8
pipenv install django
```
+ Створюєм новий проект.
```
django-admin startproject first_site
``` 
+  Запускаєм сервер і переходимо за посиланням для перевірки роботи (127.0.0.1:8000):
+  Сервер працює без помилок.
```
python manage.py runserver
```
+ Створим новий додаток
```
python manage.py startapp main
```
+ В новоствореній директорії, додаємо файли `index.html` та `urls.py`.

+ Вказуэмо шлях до веб-сторінок. 
```
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

+ Заповнюємо файл urls.py
```
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'health/', views.health, name='health')
]
```

+ Встановлюєм модуль `requests` для pipenv
```
pipenv install requests
```
+ Скрипти, добавлені у Pipfile
+ Додав логування при помилці
