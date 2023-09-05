# Generated by Django 4.2.4 on 2023-09-04 23:26

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('nm_first', models.CharField(max_length=50, null=True)),
                ('nm_last', models.CharField(max_length=50, null=True)),
                ('nm_complete', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('date_birth', models.DateField(null=True)),
                ('image', models.FileField(default='photo/no-photo.png', null=True, upload_to='photo/user')),
                ('sex_code', models.CharField(max_length=200, null=True)),
                ('sex_type', models.CharField(max_length=200, null=True)),
                ('occupation_code', models.CharField(max_length=200, null=True)),
                ('occupation_type', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'funcionario',
            },
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('type_account', models.CharField(default='usr', max_length=200, null=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('is_staff', models.BooleanField(default=False, null=True)),
                ('is_update_session', models.BooleanField(default=False, null=True)),
                ('is_first_login', models.BooleanField(default=True, null=True)),
                ('is_reset_password', models.BooleanField(default=False, null=True)),
                ('default_password', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nm_first', models.CharField(max_length=200, null=True)),
                ('nm_last', models.CharField(max_length=200, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='%(app_label)s_%(class)s_user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_login.user')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='%(app_label)s_%(class)s_user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'funcionario_login',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
