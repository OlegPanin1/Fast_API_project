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

