# mushrooms_on_fastapi

Все действия выполняются в папке с проектом.

## Для сборки и запуска Docker

Для запуска введите в терминале две команды:

```
docker build . --tag fastapi_app
docker run -p 8000:8000 fastapi_app
```

Или одну команду:

```
docker build . --tag fastapi_app && docker run -p 8000:8000 fastapi_app
```

После запуска перейдите по адресу http://0.0.0.0:8000/docs, чтобы протестировать API.
Перейдите по адресу http://0.0.0.0:8000/redoc, чтобы посмотреть документацию API

Если порт 8000 уже занят, то нужно указать любой другой свободный.

## Для сборки и запуска через virtual environment (python 3.12)

В терминале выполняем последовательно следующие команды:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app
```

После запуска перейдите по адресу http://127.0.0.1:8000/docs, чтобы протестировать API
Перейдите по адресу http://127.0.0.1:8000/redoc, чтобы посмотреть документацию API
