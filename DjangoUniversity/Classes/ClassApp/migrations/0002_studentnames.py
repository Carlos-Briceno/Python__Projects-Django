# Generated by Django 3.2 on 2021-04-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('grade', models.IntegerField(default='', max_length=12)),
            ],
        ),
    ]
