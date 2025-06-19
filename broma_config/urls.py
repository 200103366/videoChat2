from django.contrib import admin
from django.urls import path, include
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("conversations/", include("conversations.urls")),
    path("", include("core.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # только один include
]

