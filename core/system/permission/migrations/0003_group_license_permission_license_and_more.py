# Generated by Django 4.2.5 on 2023-09-24 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0004_license_account_people_license_owner_account'),
        ('permission', '0002_alter_group_table_alter_permission_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='license',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='license.license'),
        ),
        migrations.AddField(
            model_name='permission',
            name='license',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='license.license'),
        ),
        migrations.AddField(
            model_name='permissiongroup',
            name='license',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='license.license'),
        ),
    ]
