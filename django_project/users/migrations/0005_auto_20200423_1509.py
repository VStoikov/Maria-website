# Generated by Django 3.0.4 on 2020-04-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200423_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(default='https://www.facebook.com'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(default='https://www.instagram.com'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.URLField(default='https://www.twitter.com'),
        ),
    ]
