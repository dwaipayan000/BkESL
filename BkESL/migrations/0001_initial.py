# Generated by Django 3.1.1 on 2020-09-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('sdo', models.CharField(max_length=20)),
                ('sharing', models.CharField(max_length=20)),
                ('gss', models.CharField(max_length=20)),
                ('feeder', models.CharField(max_length=20)),
                ('kwh', models.CharField(max_length=20)),
            ],
        ),
    ]
