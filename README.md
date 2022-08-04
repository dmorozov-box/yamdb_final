# Проект api_yamdb

## Описание

YaMDb собирает отзывы (Review) пользователей на произведения (Title).
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий (Category) и жанров (Genre) может быть расширен
Отзывы могут комментироваться пользователями (Comments) 

Сайт настроен для запуска на localhost в docker-compose и имеет 3 контейнера: 
- db - база данных Postgres SQL
- web - собственно сам проект YaMDb на Django
- nginx - веб сервер

## Развертывание проекта

### Шаблон наполнения файла переменных окружения .env
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```

### Команды запуска проекта в Docker

1. Собрать и запустить образы
```
docker-compose up -d --build
```
2. Выполнить миграции, создать суперпользователя и собрать статику в контейнере
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
Заполнение базы начальными данными
```
docker-compose exec web python manage.py loaddata fixtures.json
```

Посмотреть документацию проекта можно по ссылке http://localhost/redoc/

Для остановки контейнеров воспользуйтесь командой
```
docker-compose down -v
```
