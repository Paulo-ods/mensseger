# Generated by Django 4.2.5 on 2023-09-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_hour_id_alter_hour_cd_hour_minute'),
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramMessagesHourRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(null=True)),
                ('dateModification', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('hour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.hour')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='telegram.telegrammessages')),
            ],
            options={
                'db_table': 'telegram_message_hour',
            },
        ),
    ]
