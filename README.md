# mushrooms_on_fastapi

Все действия выполняются в папке с проектом.

## Для сборки и запуска Docker

Для запуска введите в терминале две команды:

```
docker build . --tag fastapi_app
docker run -p 80:80 fastapi_app
```

Или одну команду:

```
docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app
```

После запуска перейдите по адресу http://0.0.0.0:8000/docs#/

## Для сборки и запуска без Docker

В терминале выполняем последовательно следующие команды:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app
```

После запуска перейдите по адресу http://0.0.0.0:8000/docs#/
