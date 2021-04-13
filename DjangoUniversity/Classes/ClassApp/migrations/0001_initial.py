# Generated by Django 3.2 on 2021-04-13 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
                ('course', models.IntegerField(default='', max_length=60)),
                ('instructor', models.CharField(default='', max_length=60)),
                ('duration', models.FloatField(default=0)),
            ],
        ),
    ]
