# Generated by Django 3.0.2 on 2020-02-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item_acquisition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='acquisition_date',
            field=models.DateField(),
        ),
    ]