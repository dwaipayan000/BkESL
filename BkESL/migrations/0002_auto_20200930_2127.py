# Generated by Django 3.1.1 on 2020-09-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='kwh',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='sharing',
            field=models.CharField(max_length=3),
        ),
    ]
