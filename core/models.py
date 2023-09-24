from django.db import models


# Create your models here.

class Log(models.Model):
    dateCreated = models.DateTimeField(null=True)
    dateModification = models.DateTimeField(null=True)
    status = models.BooleanField(null=True, default=True)

    class Meta:
        abstract = True


class LogLicense(Log):
    license = models.ForeignKey('license.License', on_delete=models.DO_NOTHING, null=True)

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


class Hour(Log):
    cd_hour_minute = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200, null=True)
    hour = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)
    hour_minute = models.TimeField(null=True)

    class Meta:
        db_table = 'hour'


class Module(Log):
    module = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=512, null=True)
    module_parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='self_module')

    class Meta:
        db_table = 'module'
