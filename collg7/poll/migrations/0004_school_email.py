# Generated by Django 4.0.4 on 2022-06-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_school_male'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
    ]
