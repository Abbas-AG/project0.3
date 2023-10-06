# Generated by Django 4.2.5 on 2023-09-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0002_room_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeebreak',
            name='picture',
            field=models.ImageField(null=True, upload_to='coffee_breaks/'),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='image',
            field=models.ImageField(null=True, upload_to='special_offers/'),
        ),
    ]
