<div id="header" align="center">
  <h1>Проект my_opinion</h1>
</div>

## Что это за проект, какую задачу он решает, в чём его польза;
> [!NOTE]
> Создава посты, коментировать посты свои и чужие.
> Подписываться на интересых авторизованных пользователей.
> Создаваать новые токен для безовасного входа на сервер (Токен действует сутки)

## Как развернуть проект на локальной машине.
> [!IMPORTANT]
> * [1] (Клонируем проект) :git clone git@github.com:OsKaLis/my_opinion.git
> * [2] (Переходим в директорию проекта) :cd my_opinion/
> * [3] (Устанавливаем изарированое окружение) :python -m venv venv 
> * [4] (Запускаем изалированное окружение, в разных операционках запускается по разному,
>   этот вариант черес ОС Windows 10 Pro консол Git Bash Here) :source venv/Scripts/activate
> * [5] (Обновляем pip до актуальной версии) : python -m pip install --upgrade pip
> * [6] (Устанавливаем нужное для работы) :pip install -r requirements.txt
> * [7] (Переходим в yatube_api/, сам проект) :cd yatube_api/
> * [8] (Запускаем миграцию баз) : python manage.py migrate
> * [9] (Запуск проекта) :python manage.py runserver
> * [10] (По умолчанию нужно перейти по адресу) :http://127.0.0.1:8000/api/v1/
> * [11] (По всем запросам есть документация) :http://127.0.0.1:8000/redoc/#tag/api

## Cтек технологий:
<img src="https://img.shields.io/badge/Python_-3.9.10-Green">  <img src="https://img.shields.io/badge/SQLite_-3.41.2-steelblue">  <img src="https://img.shields.io/badge/django_-3.2-Green">
<img src="https://img.shields.io/badge/djangorestframework_-3.12.4-Green">

## Некоторые примеры запросов к my_opinion.
Запрос ковсем постам созданые на этом сервере, [GET] :http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=0

Создание новый пост авторизованным пользователем, [POST] :http://127.0.0.1:8000/api/v1/posts/
```
rew JSON:
{
  "text": "Ьшк",
  "group": 2
}
```

Создание токена, [POST] :http://127.0.0.1:8000/api/v1/jwt/create/
```
rew JSON:
{
    "username": "lisa",
    "password": "sFPRojyq"
}
```

## Автор: Юшко Ю.Ю.
