# Generated by Django 3.1.1 on 2020-10-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0007_auto_20201004_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billed_unit',
            name='ht',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='billed_unit',
            name='lt',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='billed_unit',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='kwh',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='eht_consumer_unit',
            name='billed_unit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='overall_loss',
            name='T_D',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='overall_loss',
            name='consumption',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='overall_loss',
            name='energy_billed',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
