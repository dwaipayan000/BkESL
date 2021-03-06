# Generated by Django 3.1.1 on 2020-10-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0003_auto_20200930_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billed_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('sdo', models.CharField(max_length=20)),
                ('ht', models.CharField(max_length=20)),
                ('lt', models.CharField(max_length=20)),
                ('total', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EHT_consumer_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('sdo', models.CharField(max_length=20)),
                ('consumer_name', models.CharField(max_length=20)),
                ('billed_unit', models.CharField(max_length=20)),
            ],
        ),
    ]
