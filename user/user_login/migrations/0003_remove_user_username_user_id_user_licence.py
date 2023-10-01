# Generated by Django 4.2.5 on 2023-09-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0002_alter_user_table_alter_userlogin_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='licence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
