# Generated by Django 3.1.1 on 2020-10-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0024_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='home',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
    ]
