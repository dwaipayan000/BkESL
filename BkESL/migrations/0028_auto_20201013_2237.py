# Generated by Django 3.1.1 on 2020-10-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0027_auto_20201012_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billed_unit',
            name='sl_no',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='sl_no',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='eht_consumer_unit',
            name='sl_no',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='vigilance_data',
            name='sl_no',
            field=models.ImageField(upload_to=''),
        ),
    ]
