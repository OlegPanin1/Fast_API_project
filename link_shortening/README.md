# Сервис сокращения URL

## Описание

Сервис сокращения URL (Short URL): Позволяет создавать короткие ссылки для длинных URL, перенаправлять по короткому идентификатору и предоставлять информацию о ссылке.

 ## Файлы
- main.py - Основной код приложения
- Dockerfile - Dockerfile для сборки образа
- requirements.txt - Зависимости проекта
- README.md - Документация проекта
- shorturl.db - База данных SQLite

## Эндпоинты:
- POST /shorten: Принимает полный URL (JSON: {“url”:"…"}) и возвращает короткую ссылку.
- GET /{short_id}: Перенаправляет на полный URL, если он существует.
- GET /stats/{short_id}: Возвращает JSON с информацией о полном URL.

## Инструкция

- Клонировать проект с репозитория GitHub: ``` git clone https://github.com/логин/todo-service.git ```
- Установить зависимости: pip install ``` -r requirements.txt ```
- Запустить сервер локально ``` uvicorn main:app --reload --port 8003 ```
- Открыть в браузере: ``` http://127.0.0.1:8003/docs ```

## Запуск через Docker

- Собрать Docker-образ: ``` docker build -t shorturl-service -f Dockerfile.txt . ```
- Запустить контейнер: ``` docker run -d -p 8003:80 -v shorturl_data:/app/data shorturl-service ```
- Открыть в браузере: ``` http://127.0.0.1:8003/docs ```

##Примеры:
- POST /shorten: Принимает полный URL (JSON: {“url”:"…"}) и возвращает короткую ссылку.
![image](https://github.com/user-attachments/assets/b31de943-eaec-4661-abef-4b4684a0c731)
- GET /{short_id}: Перенаправляет на полный URL, если он существует.
![image](https://github.com/user-attachments/assets/2b366404-6238-4345-a358-41491486122b)
- GET /stats/{short_id}: Возвращает JSON с информацией о полном URL.
![image](https://github.com/user-attachments/assets/fb1d6c99-f894-48d7-8997-ee40565bc367)


