# Generated by Django 5.0 on 2024-01-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_bodydata_profile_meal_amount_meal_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='favorited',
            field=models.BooleanField(default=False),
        ),
    ]
