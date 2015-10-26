#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


from main.models import Cereal, Manufacturer

print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cereals.csv"

#print "%s%s" % (dir_name, file_name)
#print "{0}/{1}".format(dir_name, file_name)

cereals_csv = os.path.join(dir_name, file_name)

print cereals_csv
csv_file = open(cereals_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_man, created = Manufacturer.objects.get_or_create(manufacturer=row['Manufacturer'])
    new_man.man_pic = "/media/man_pic/"+new_man.manufacturer.replace(' ', '')+".png"
    print new_man.man_pic
    new_man.save()

    new_cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'].replace('_', ' '))
    print new_cereal.name
    new_cereal.manufacturer = new_man
    print new_cereal.manufacturer
    new_cereal.cereal_type = row['Type']
    new_cereal.calories = row['Calories']
    new_cereal.protein = row['Protein (g)']
    new_cereal.fat = row['Fat']
    new_cereal.sodium = row['Sodium']
    new_cereal.fiber = row['Dietary Fiber']
    new_cereal.carbs = row['Carbs']
    new_cereal.sugars = row['Sugars']
    new_cereal.shelf = row['Display Shelf']
    print new_cereal.shelf
    new_cereal.potassium = row['Potassium']
    new_cereal.vits_and_mins = row['Vitamins and Minerals']
    new_cereal.serving_size_weight = row['Serving Size Weight']
    new_cereal.cups_per_serving = row['Cups per Serving']
    new_cereal.cereal_pic = "/media/cereal_pic/"+new_cereal.name.replace(' ', '').replace('%', '')+".jpg"
    print new_cereal.cereal_pic
    new_cereal.save()

csv_file.close()






