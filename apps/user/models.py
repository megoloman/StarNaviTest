from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser

from core.models import BaseModel
from apps.user.managers import UserManager


class User(AbstractUser, BaseModel):
    github_id = models.PositiveIntegerField(_('github id'), blank=True, null=True)
    github_name = models.CharField(_('github name'), max_length=200, blank=True, null=True)

    objects = UserManager()
