from django.db import models

import core.models


# Create your models here.

class License(core.models.Log):
    token = models.UUIDField()
    activate_date = models.DateTimeField()
    limit_date = models.DateTimeField()
    category = models.ForeignKey('LicenseCategory', on_delete=models.DO_NOTHING, null=True)
    active = models.CharField(default=False)
    payment = models.ForeignKey('LicensePayment', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'license'


class LicenseCategory(core.models.Log):
    type_name = models.CharField(max_length=255, primary_key=True)
    description_name = models.CharField(max_length=255, null=True)
    subcategory = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    time = models.IntegerField(null=True)
    active = models.CharField(default=False)

    class Meta:
        db_table = 'license_category'


class LicensePayment(core.models.Log):
    class Meta:
        db_table = 'license_payment'


