from django.db import models

import core.models


class Permission(core.models.LogLicense):
    permission = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=512, null=True)
    order = models.IntegerField(null=True)
    module = models.ForeignKey('core.Module', on_delete=models.DO_NOTHING, null=True, related_name="module_system")
    permission_parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True,
                                          related_name='self_permission')

    class Meta:
        db_table = 'system_permission'


class Group(core.models.LogLicense):
    group = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=512, null=True)
    order = models.IntegerField(null=True)
    group_parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='self_group')

    class Meta:
        db_table = 'system_group'


class PermissionGroup(core.models.LogLicense):
    permission = models.ForeignKey('Permission', on_delete=models.DO_NOTHING, null=True,
                                   related_name='permission_group')
    group = models.ForeignKey('Group', on_delete=models.DO_NOTHING, null=True, related_name='group_permission')

    class Meta:
        db_table = 'system_permission_group_related'


#
class GroupUser(core.models.Log):
    user = models.ForeignKey('user_login.User', on_delete=models.DO_NOTHING, null=True)
    group = models.ForeignKey('Group', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'system_group_user_related'


class PermissionUser(core.models.Log):
    user = models.ForeignKey('user_login.User', on_delete=models.DO_NOTHING, null=True)
    permission = models.ForeignKey('Permission', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'system_permission_user_related'
