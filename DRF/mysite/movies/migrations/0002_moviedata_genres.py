# Generated by Django 5.0.4 on 2024-04-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genres',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
