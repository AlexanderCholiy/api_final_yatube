# API_YATUBE

## Описание
**api_yatube** — это RESTful API для социальной сети Yatube.\
С его помощью пользователи могут создавать посты и комментировать их.

## Функционал:
- Регистрация пользователей и аутентификация по токену
- CRUD-операции для постов и комментариев
- Подписка и отписка от других пользователей
- Просмотр сообществ

## Установка и запуск

### 1. Клонируйте репозиторий:
```
git clone https://github.com/AlexanderCholiy/api_final_yatube.git
```
> bash
### 2. Перейдите в корневую папку:
```
cd api_final_yatube
```
> bash
### 3. Установите виртуальное окружение и зависимости:
- Для Windows:
```
. .\venv\Scripts\activate
```
- Для Linux или MacOS:
```
. ./venv/bin/activate
```
- Установите зависимости:
```
pip install -r requirements.txt
```
> bash
### 4. Примените миграции и создайте суперпользователя:
```
cd yatube_api
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
> bash
### 5. Запустите сервер:
```
python manage.py runserver
```
> bash

## Ключевые моменты
  - Для аутентификации используется JWT-токены.
  - У неаутентифицированных пользователей доступ к API только на чтение.
  Исключение — эндпоинт `/follow/`: доступ к нему предоставляться только
  аутентифицированным пользователям.
  - Аутентифицированным пользователям разрешено изменение и удаление своего
  контента; в остальных случаях доступ предоставляется только для чтения.

### Документация для API Yatube
http://127.0.0.1:8000/redoc/

### Пример запроса
- **Получение JWT токена:**
  - **Метод:** $${\color{orange}POST}$$
  - **Эндпоинт:** api/v1/api-token-auth/
  - **Тело запроса:**
  ```json
  {
    "username": "your_login",
    "password": "your_password"
  }
  ```
  - **Пример ответа:**
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDk0MTQ3NywianRpIjoiODUzYzE5MTg5NzMwNDQwNTk1ZjI3ZTBmOTAzZDcxZDEiLCJ1c2VyX2lkIjoxfQ.0vJBPIUZG4MjeU_Q-mhr5Gqjx7sFlO6AShlfeINK8nA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwODU1Mzc3LCJqdGkiOiJkY2EwNmRiYTEzNWQ0ZjNiODdiZmQ3YzU2Y2ZjNGE0YiIsInVzZXJfaWQiOjF9.eZfkpeNVfKLzBY7U0h5gMdTwUnGP3LjRn5g8EIvWlVg"
  } 
  ```
  Токен вернётся в поле access, а данные из поля refresh пригодятся для
  обновления токена.\
  При каждом запросе к API нужно в заголовке запроса, в поле Authorization,
  передавать основной токен доступа, полученный в поле access. Перед самим
  токеном должно стоять ключевое слово Bearer и пробел: Bearer токен

### Автор
**Чолий Александр** [[Telegram](https://t.me/alexander_choliy)]

### Рекомендации
_Проверять и отлаживать работу API удобно через **Postman**._\
_Эта программа умеет отправлять запросы, анализировать ответы и сохранять запросы для повторного применения в будущем._
