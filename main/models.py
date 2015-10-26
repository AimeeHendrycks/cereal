from django.db import models

# Create your models here.
class Manufacturer(models.Model):

    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    man_pic = models.ImageField(upload_to='man_pic', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.manufacturer

class Cereal(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    manufacturer = models.ForeignKey('main.Manufacturer', null=True, blank=True)
    cereal_type = models.CharField(max_length=255, null=True, blank=True)
    calories = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    shelf = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    vits_and_mins = models.FloatField(null=True, blank=True)
    serving_size_weight = models.FloatField(null=True, blank=True)
    cups_per_serving = models.FloatField(null=True, blank=True)
    cereal_pic = models.ImageField(upload_to='cereal_pic', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name


