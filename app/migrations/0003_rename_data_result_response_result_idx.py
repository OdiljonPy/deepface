# Generated by Django 4.1.3 on 2023-01-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='data',
            new_name='response',
        ),
        migrations.AddField(
            model_name='result',
            name='idx',
            field=models.IntegerField(default=0),
        ),
    ]
