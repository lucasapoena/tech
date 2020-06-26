# Generated by Django 3.0.7 on 2020-06-25 23:54

from django.db import migrations

def populate_processors(apps, schema_editor):

    Processor = apps.get_model('app', 'processor')
    [
        Processor(processor="Intel Core i5", processor_brand="Intel").save(),
        Processor(processor="Intel Core i7", processor_brand="Intel").save(),
        Processor(processor="AMD Ryzen 7", processor_brand="AMD").save(),
        Processor(processor="AMD Athlon", processor_brand="AMD").save()
    ]

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_processors)
    ]
