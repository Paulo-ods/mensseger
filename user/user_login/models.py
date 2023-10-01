from django.contrib.auth.models import UserManager
from django.db import models
from user.models import Profile, PersonMeta
import core.models


# Create your models here.

class UserLogin(Profile):
    user = models.OneToOneField('User', on_delete=models.DO_NOTHING, null=True)
    nm_first = models.CharField(max_length=200, null=True)
    nm_last = models.CharField(max_length=200, null=True)
    objects = UserManager()

    class Meta:
        db_table = 'user_login'


class User(core.models.Log, PersonMeta):
    licence = models.ForeignKey('license.License', on_delete=models.DO_NOTHING, null=True)
    # empresa = models.ForeignKey('empresa.Empresa', on_delete=models.DO_NOTHING, null=True, related_name='empresa_user')
    # endereco = models.ForeignKey('core.Endereco', on_delete=models.DO_NOTHING, null=True, related_name='endereco')

    class Meta:
        db_table = 'user'
