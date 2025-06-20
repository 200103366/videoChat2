import uuid

#from accounts.models import User
from django.contrib.auth.models import User
from django.db import models
from django.db.models.constraints import CheckConstraint
from django.db.models.expressions import F
from django.db.models.query_utils import Q
from django.utils.translation import gettext_lazy as _


class Conversation(models.Model):
    """
    This model represents a room for chatting, video call and game between two users.
    """

    id = models.UUIDField(_("conversation id"), primary_key=True, default=uuid.uuid4)

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_conversations",
    )
    invitee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="joined_conversations",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    finished_at = models.DateTimeField(null=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(creator=F("invitee")),
                name="check_creator_invitee_not_same",
            )
        ]


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")

    content = models.TextField(_("content"), blank=False, null=False)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
