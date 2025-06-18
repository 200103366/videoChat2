# Используем свежий Python
FROM python:3.11-slim

# Отключаем буферизацию вывода
ENV PYTHONUNBUFFERED=1

# Обновляем систему и ставим необходимые библиотеки
RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем оставшийся код
COPY . .

# Собираем статику (важно!)
RUN python manage.py collectstatic --noinput

# Команда запуска (миграции + запуск сервера)
CMD ["sh", "-c", "python manage.py migrate && daphne -b 0.0.0.0 -p 8000 broma_config.asgi:application"]
