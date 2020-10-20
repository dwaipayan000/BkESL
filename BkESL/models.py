from django.db import models

class Consumption(models.Model):
    month=models.CharField(max_length=20)
    sl_no=models.IntegerField()
    sdo=models.CharField(max_length=20)
    sharing=models.FloatField(max_length=3)
    gss=models.CharField(max_length=20)
    feeder=models.CharField(max_length=20)
    kwh=models.IntegerField()

    def __str__(self):
        return self.month
class Billed_unit(models.Model):
    month=models.CharField(max_length=20)
    sl_no=models.IntegerField()
    sdo=models.CharField(max_length=20)
    ht=models.IntegerField()
    lt=models.IntegerField()
    total=models.IntegerField()
    def __str__(self):
        return self.month
class Eht_consumer_unit(models.Model):
    month=models.CharField(max_length=20)
    sl_no=models.IntegerField()
    sdo=models.CharField(max_length=20)
    consumer_name=models.CharField(max_length=20)
    billed_unit=models.IntegerField()
    def __str__(self):
        return self.month
class Vigilance_data(models.Model):

    month = models.CharField(max_length=20)
    sl_no=models.IntegerField()
    sdo = models.CharField(max_length=20)
    unit = models.IntegerField(default=0)

    def __str__(self):
        return self.month
class Image(models.Model):
    home=models.ImageField(upload_to='post_image',blank=True)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


