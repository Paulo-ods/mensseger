# Generated by Django 4.2.5 on 2023-10-01 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_login.user'),
        ),
    ]
