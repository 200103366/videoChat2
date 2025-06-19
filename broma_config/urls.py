from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),       # теперь доступно по /accounts/login/
    path("conversations/", include("conversations.urls")),
    path("", include("core.urls")),                    # корневые маршруты пусть будут из core
]
