# Generated by Django 3.1.1 on 2020-10-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0012_auto_20201006_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='kwh',
            field=models.IntegerField(max_length=10),
        ),
    ]
