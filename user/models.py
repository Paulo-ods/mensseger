from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, Permission, Group, PermissionsMixin
from django.utils.translation import gettext_lazy as _

import core.models
from django.db import models


# Create your models here.
class Profile(AbstractBaseUser, core.models.Log, PermissionsMixin):
    type_account = models.CharField(null=True, max_length=200, default='usr')
    username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(null=True, default=False)
    is_update_session = models.BooleanField(default=False, null=True)
    is_first_login = models.BooleanField(default=True, null=True)
    is_reset_password = models.BooleanField(default=False, null=True)
    default_password = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=200, null=True)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )

    class Meta:
        abstract = True


class PersonMeta(models.Model):
    nm_first = models.CharField(max_length=50, null=True)
    nm_last = models.CharField(max_length=50, null=True)
    nm_complete = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    # cpf = models.CharField(max_length=11, null=True)
    # cpf_form = models.CharField(max_length=14, null=True)
    # cnpj = models.CharField(max_length=14, null=True)
    # cnpj_form = models.CharField(max_length=18, null=True)
    # rg = models.CharField(max_length=8, null=True)
    # rg_form = models.CharField(max_length=11, null=True)
    date_birth = models.DateField(null=True)
    image = models.FileField(upload_to='photo/user', default='photo/no-photo.png', null=True)
    sex_code = models.CharField(null=True, max_length=200)
    sex_type = models.CharField(null=True, max_length=200)

    occupation_code = models.CharField(null=True, max_length=200)
    occupation_type = models.CharField(null=True, max_length=200)

    class Meta:
        abstract = True
