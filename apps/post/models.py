from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from core.models import BaseModel


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(_('text'), max_length=500)
    likes = models.PositiveIntegerField(_('likes'), default=0)
    dislikes = models.PositiveIntegerField(_('dislikes'), default=0)
