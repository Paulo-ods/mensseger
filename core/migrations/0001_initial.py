# Generated by Django 4.2.4 on 2023-09-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('code', models.CharField(max_length=255, null=True)),
                ('config', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('order', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'config',
            },
        ),
        migrations.CreateModel(
            name='IntegrationKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('path', models.CharField(max_length=255, null=True)),
                ('module', models.CharField(max_length=255, null=True)),
                ('token', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'integration_keys',
            },
        ),
    ]