# bewiseTZ
Тестовое задание

## Запуск

```docker-compose up --build```

## Docker-compose
Содержит два контейнера. Контейнер с приложением и с бд postgres. Контейнер базы данных содержит volume, что позволяет сохранять данные после остановки работы контейнера.

## Директория app
* crud.py - 
* database.py - подключение к бд, создание таблиц
* main.py - входная точка приложения FastAPi
* requirements.txt - зависимости проекта

## Маршруты
* POST запрос localhost:8000/add  - принимает необходимое количество вопросов для добавления в бд, получает вопросы в виде json, фильтрует необходимые параметры, возращает нужное количество вопросов, которые еще не были добавлены в бд, которых еще не было в бд
* GET запрос localhost:8000/show - вывод всех вопросов

## Примеры запроса
*С помощью curl
 ```curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 20}' http://localhost:8000/add ```
