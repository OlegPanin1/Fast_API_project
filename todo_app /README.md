# TODO-сервис

## Описание

TODO-сервис: Реализует CRUD-операции для списка задач с хранением данных в SQLite.

## Эндпоинты:
1. POST /items: Создание задачи (title, description?,
completed=false).
2. GET /items: Получение списка всех задач.
3. GET /items/{item_id}: Получение задачи по ID.
4. PUT /items/{item_id}: Обновление задачи по ID.
5. DELETE /items/{item_id}: Удаление задачи.

## Инструкция

### Локальный запуск
Установите зависимости: pip install -r requirements.txt
Запустите сервер: uvicorn main:app --reload
Откройте в браузере: http://127.0.0.1:8000/docs

Запуск через Docker
Сборка Docker-образа: docker build -t todo-service .
Запуск контейнера: docker run -d -p 8000:80 -v todo_data:/app/data todo-service
Запуск в браузере: http://127.0.0.1:8000/docs
