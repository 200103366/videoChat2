from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("create_conversation/", views.create_conversation, name="create-conversation"),
    path("join_conversation/", views.join_conversation, name="join-conversation"),
    path("find_conversation/", views.find_conversation, name="find-conversation"),
    path("<uuid:id>/", views.view_conversation, name="view-conversation"),  # ✅ без лишнего "conversations/"
]
