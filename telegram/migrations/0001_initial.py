# Generated by Django 4.2.4 on 2023-09-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('cd_chat', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=512)),
                ('type_code', models.CharField(default='group', max_length=255, null=True)),
                ('type_config', models.CharField(default='TELEGRAM-CHAT', max_length=255, null=True)),
            ],
            options={
                'db_table': 'telegram_chat',
            },
        ),
        migrations.CreateModel(
            name='TelegramMessagesCategory',
            fields=[
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('category', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=512, null=True)),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_parent', to='telegram.telegrammessagescategory')),
            ],
            options={
                'db_table': 'telegram_messages_category',
            },
        ),
        migrations.CreateModel(
            name='TelegramMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('message', models.CharField(max_length=4096, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_message', to='telegram.telegrammessagescategory')),
            ],
            options={
                'db_table': 'telegram_messages',
            },
        ),
    ]
