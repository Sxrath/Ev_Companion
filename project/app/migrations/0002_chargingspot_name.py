# Generated by Django 4.2.7 on 2023-12-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingspot',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
