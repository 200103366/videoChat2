import environ

from .local import *

# Создаём env instance
env = environ.Env(
    DEBUG=(bool, False),
)

# ЧИТАЕМ переменные из .env или окружения Render
environ.Env.read_env()  # 🔥 это нужно!

# Настройки
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")

DATABASES = {
    "default": env.db(),
}

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

REDIS_URL = env("REDIS_URL")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    }
}
