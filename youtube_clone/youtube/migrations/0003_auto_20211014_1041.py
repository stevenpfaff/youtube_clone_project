# Generated by Django 3.2.8 on 2021-10-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20211014_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
