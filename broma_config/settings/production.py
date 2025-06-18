import environ
from pathlib import Path

# === Базовая директория проекта ===
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# === Чтение .env ===
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file=BASE_DIR / ".env")  # работает и локально, и на сервере

# === Основные настройки ===
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[".onrender.com", "localhost", "127.0.0.1"])

# === Установленные приложения ===
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "accounts",
    "conversations",
]

# === Middleware ===
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === URL и ASGI ===
ROOT_URLCONF = "broma_config.urls"
ASGI_APPLICATION = "broma_config.asgi.application"

# === Templates ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # при необходимости
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === База данных ===
DATABASES = {
    "default": env.db(),  # Пример: postgres://USER:PASSWORD@HOST:PORT/DBNAME
}

# === Redis и Channels ===
REDIS_URL = env("REDIS_URL")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

# === Статические файлы ===
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# === Часовой пояс и язык ===
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
