FROM python:3.12-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Для запуска введите две команды:
# docker build . --tag fastapi_app
# docker run -p 80:80 fastapi_app

# Или одной командой
# docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app