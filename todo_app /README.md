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
- Установить зависимости: pip install -r requirements.txt
- Запустить сервер: uvicorn main:app --reload
- Открыть в браузере: http://127.0.0.1:8000/docs

### Запуск через Docker
- Сборка Docker-образа: docker build -t todo-service .
- Запустить контейнер: docker run -d -p 8000:80 -v todo_data:/app/data todo-service
- Открыть в браузере: http://127.0.0.1:8001/docs
