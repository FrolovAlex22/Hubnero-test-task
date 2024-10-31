# Тестовое задание для Hubnero

## Техническое задание

В качестве тестового задания тебе необходимо создать базовый Django проект, который при вызове "/get-current-usd/" будет возвращать актуальный курс доллара к рублю в формате JSON и 10 последних запросов курсов. Для получения курса используйте внешнее API (выберите подходящее самостоятельно). Между каждым запросом курса должна быть пауза не менее 10 секунд.

1. Разбить на подзадачи
2. Реализовать на Django
3. Подготовить блок вопросов, которые бы ты задал:
- продакт менеджеру
- TL
4. Подготовить тайминги по компонентам:
- первичная оценка
- фактическое время выполнения

## Вопросы для PM, TL

   - Вопросы для продакт-менеджера:
     - Планируеться введение модели пользователя
     - В дальнейшем подразумеваеться возможность Выбора валюты
     - Функция оповещения пользователя. Подключение websocket

   - Вопросы для Team Lead:
     - Кэширование данных с помощью Redis
     - Журнал ошибок. Настроить логирование
     - Обернуть проект в Docker
     - Решить проблему с переполнением БД

## Описание проекта

- При переходе по URL http://127.0.0.1/get-current-usd/, создаеться запрос к внешнему API для получения актуального курса
- Полученые данные сохраняються в кэше.
- В кэше комплектуеться список из данных полученных после запросов к внешнему API. До 10 запросов, если запросов больше список обновляеться в хронологическом порядке.
- Пользователю возвращаеться сформировавшийся в кэше список.
- В случае если после последнего запроса прошло менее 10 секунд, пользователь получает предупреждение - "attention" о том что с последнего запроса прошло менее 10 секунд, и список последних курсов сформированный в кэше.

## Технологии
[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?logo=PostgreSQL&logoColor=white/)](https://www.postgresql.org/)
[![Django](https://img.shields.io/badge/Django-%23092E20?logo=django)](https://www.djangoproject.com/)

## Запуск проекта локально

Клонируйте репозиторий и перейдите в него:

```
git@github.com:FrolovAlex22/Hubnero-test-task.git
```

Создайте виртуальное окружение:
```
cd Hubnero-test-task

python -m venv venv
```
Активируйте виртуальное окружение:
```
Windows: source venv/Scripts/activate
Linux/macOS: source venv/bin/activate
```
Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
В корне проекта создайте файл .env по образцу:
```
.env.example
```
перейти в директорию приложения currency_rate:
```
cd currency_rate
```
Выполните миграции:
```
python manage.py migrate
```
Запустить локальный сервер:
```
python manage.py runserver
```

### Автор:

Фролов Александр
email: frolov.bsk@yandex.ru
telegram: https://t.me/frolov_bsk
