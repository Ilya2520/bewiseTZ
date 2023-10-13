# bewiseTZ
Тестовое задание

## Запуск
Клонирование репозитория
```
git clone https://github.com/Ilya2520/MyFastAPIproject2.git
cd MyFastAPIproject2
```
- В Pycharm открыть File -> settings -> python interpreter, добавить New enviroment
- Перейти в коммандной строке Windows в директорию проекта и запустить команду:
  ```
  venv\Scripts\activate
  ```
- Далее выполнить следующую команду
```
docker-compose up --build
```

## Docker-compose
Содержит два контейнера. Контейнер с приложением и с бд postgres. Контейнер базы данных содержит volume, что позволяет сохранять данные после остановки работы контейнера.

## Директория app
* crud.py - реализована логика маршрутов
* database.py - подключение к бд, создание таблиц
* main.py - входная точка приложения FastAPi
* requirements.txt - зависимости проекта

## Маршруты
* POST запрос localhost:8000/add  - принимает необходимое количество вопросов для добавления в бд, получает вопросы в виде json, фильтрует необходимые параметры, возращает нужное количество вопросов, которые еще не были добавлены в бд, которых еще не было в бд
* GET запрос localhost:8000/show - вывод всех вопросов

## Примеры запроса
* С помощью curl
 ``` curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 20}' http://localhost:8000/add ```
* Postman   указать url  http://localhost:8000/add, в качестве тела запроса передать следующий json {"questions_num": 10}
