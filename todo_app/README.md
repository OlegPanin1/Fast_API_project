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
- POST /items: Создание задачи (title, description,
completed=false).
- GET /items: Получение списка всех задач.
- GET /items/{item_id}: Получение задачи по ID.
- PUT /items/{item_id}: Обновление задачи по ID.
- DELETE /items/{item_id}: Удаление задачи.

## Инструкция

- Клонировать проект с репозитория GitHub: ``` git clone https://github.com/<ваш_логин>/todo-service.git ```
- Установить зависимости: pip install ``` -r requirements.txt ```
- Запустить сервер локально ``` uvicorn main:app --reload --port 8000 ```
- Открыть в браузере: ``` http://127.0.0.1:8000/docs ```

## Запуск через Docker

- Собрать Docker-образ: ``` docker build -t todo-service -f Dockerfile.txt . ```
- Запустить контейнер: ``` docker run -d -p 8001:80 -v todo_data:/app/data todo-service ```
- Открыть в браузере: ``` http://127.0.0.1:8001/docs ```

## Примеры 

- GET /items: Получение списка всех задач.

![image](https://github.com/user-attachments/assets/1e0f040b-8e8b-458a-9024-bf413c80156f)

- GET /items: Получение списка всех задач.

![image](https://github.com/user-attachments/assets/2c5aa708-5071-44bf-b3cd-c2851c311230)

- GET /items/{item_id}: Получение задачи по ID.

![image](https://github.com/user-attachments/assets/deea9600-da21-463c-89f6-8ecfd1b61fd4)

- PUT /items/{item_id}: Обновление задачи по ID.
- 
![image](https://github.com/user-attachments/assets/c2e07629-d621-4fa6-956a-c9c3137187e7)

- DELETE /items/{item_id}: Удаление задачи.

![image](https://github.com/user-attachments/assets/07abdcb9-bf20-4de3-9190-2d414917bf31)




