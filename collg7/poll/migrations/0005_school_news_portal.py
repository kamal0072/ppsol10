# Generated by Django 4.0.4 on 2022-06-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_school_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='news_portal',
            field=models.URLField(default='https://www.youtube.com/'),
        ),
    ]
