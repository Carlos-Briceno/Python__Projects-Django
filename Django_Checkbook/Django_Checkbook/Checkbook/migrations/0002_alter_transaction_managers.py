# Generated by Django 3.2 on 2021-04-21 20:14

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
    ]
