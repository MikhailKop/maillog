# Generated by Django 5.0.6 on 2024-09-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('int_id', models.CharField()),
                ('str', models.CharField(blank=True, null=True)),
                ('address', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created', models.DateTimeField()),
                ('id', models.CharField(primary_key=True, serialize=False)),
                ('int_id', models.CharField()),
                ('str', models.CharField()),
                ('status', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
    ]
