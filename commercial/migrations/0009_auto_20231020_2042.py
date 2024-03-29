# Generated by Django 3.2.6 on 2023-10-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
