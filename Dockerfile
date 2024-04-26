#FROM ubuntu:latest
#LABEL authors="user"
#ENTRYPOINT ["top", "-b"]

FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]