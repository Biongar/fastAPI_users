# fapi project

## Технологии

- Python
- FastAPI
- alembic
- SQLAlchemy
- PostgreSQL
- JWT
- asyncio

## О проекте

Данный проект был разработан в целях изучения нового фрэймворка и на данный момент содержит в себе:
- Создание пользователя
- Чтение пользователя/пользователей
- Изменение пользователя
- Удаление пользователя
- Авторизация(JWT)
- Настроены права доступа к CRUD(IsOwner or IsAdmin)

## Запуск проекта

### Клонируем репозиторий

``` sh
git clone https://path/to/repository.git .
```

### Создание виртуального окружения и установка зависимостей

``` sh
python3.10 -m venv venv;
source venv/bin/activate;
pip install -r requirements.txt
```

### Создание базы данных postgresql

> sudo -u postgres psql

``` sql
CREATE USER fapi_user WITH PASSWORD '1234';
CREATE DATABASE fapi_db WITH OWNER fapi_user;
```

### Настройка файла .env

``` sh
touch .env
```

Копируем пример из файла "env_example.txt" и вставляем его в файл .env

### Запуска локального сервера
``` sh
alembic upgrade head
python manage.py
```

### Создание суперпользователя

``` sh
python createsuperuser.py
```

### Документация к REST API

http://127.0.0.1:8000/docs