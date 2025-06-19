from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),       # ✅ добавь эту строку
    path("conversations/", include("conversations.urls")),
    path("", include("core.urls")),
]
