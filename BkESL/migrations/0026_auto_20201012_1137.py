# Generated by Django 3.1.1 on 2020-10-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0025_auto_20201009_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vigilance_data',
            name='unit',
            field=models.IntegerField(null=True),
        ),
    ]