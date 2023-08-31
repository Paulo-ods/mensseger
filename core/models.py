from django.db import models


# Create your models here.

class Log(models.Model):
    dateCreated = models.DateTimeField(null=True)
    dateModification = models.DateTimeField(null=True)
    status = models.BooleanField(null=True, default=True)

    class Meta:
        abstract = True


class Config(Log):
    code = models.CharField(max_length=255, null=True)
    config = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    order = models.IntegerField(null=True)

    class Meta:
        db_table = 'config'


class IntegrationKeys(Log):
    path = models.CharField(max_length=255, null=True)
    module = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'integration_keys'
