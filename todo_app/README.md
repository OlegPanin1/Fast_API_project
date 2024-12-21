# TODO-сервис

## Описание

TODO-сервис: Реализует CRUD-операции для списка задач с хранением данных в SQLite.

 ## Файлы
- main.py - Основной код приложения
- Dockerfile - Dockerfile для сборки образа
- requirements.txt - Зависимости проекта
- README.md - Документация проекта
- todo.db - База данных SQLite 

## Эндпоинты:
- POST /items: Создание задачи (title, description?,
completed=false).
- GET /items: Получение списка всех задач.
- GET /items/{item_id}: Получение задачи по ID.
- PUT /items/{item_id}: Обновление задачи по ID.
- DELETE /items/{item_id}: Удаление задачи.

## Инструкция

### Локальный запуск
- Установить зависимости: pip install -r requirements.txt
- Запустить сервер: uvicorn main:app --reload
- Открыть в браузере: http://127.0.0.1:8000/docs

### Запуск через Docker
- Сборка Docker-образа: docker build -t todo-service .
- Запустить контейнер: docker run -d -p 8000:80 -v todo_data:/app/data todo-service
- Открыть в браузере: http://127.0.0.1:8001/docs
