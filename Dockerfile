# Используем свежий Python
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Сборка статики
RUN python manage.py collectstatic --noinput

# Запуск миграций и сервера
CMD ["sh", "-c", "python manage.py migrate && daphne -b 0.0.0.0 -p $PORT broma_config.asgi:application"]
