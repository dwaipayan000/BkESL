# Generated by Django 3.1.1 on 2020-10-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0004_billed_unit_eht_consumer_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overall_loss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('sdo', models.CharField(max_length=20)),
                ('consumption', models.CharField(max_length=20)),
                ('energy_billed', models.CharField(max_length=20)),
                ('T_D', models.CharField(max_length=4)),
            ],
        ),
    ]
