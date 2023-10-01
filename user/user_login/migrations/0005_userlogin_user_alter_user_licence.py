# Generated by Django 4.2.5 on 2023-10-01 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0004_license_account_people_license_owner_account'),
        ('user_login', '0004_remove_userlogin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_login.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='licence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='license.license'),
        ),
    ]