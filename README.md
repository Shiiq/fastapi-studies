## FastAPI-Studies
___
Основная задача - поиск фильмов по заданным параметрам, такие как жанры и года выпуска.
Реализованы пагинация результатов запроса и кеширование данных из БД.  
Стек:
- Python 3.12
- FastAPI, SQLAlchemy
- Redis
- SQLite
___
#### Скачивание и запуск:
Шаг 1 - скачивание приложения
```shell
mkdir FastAPI-Movies && cd FastAPI-Movies
```
```shell
git clone https://github.com/Shiiq/fastapi-studies.git
```
Шаг 2 - сборка и запуск
```shell
cd fastapi-studies
```
```shell
docker compose up -d --build
```
___
Для работы с приложением удобнее всего будет воспользоваться возможностью FastAPI и открыть 
уже сформированную интерактивную документацию API:  
[http://127.0.0.1:12000/docs](http://127.0.0.1:12000/docs) или [http://localhost:12000/docs](http://localhost:12000/docs)
___
anjunat@yandex.ru | Kiriakov P. | 2024
___
