# Generated by Django 2.1.7 on 2019-04-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missionapp', '0004_auto_20190411_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
