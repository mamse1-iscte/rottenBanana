# Generated by Django 3.2.12 on 2022-05-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0009_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
