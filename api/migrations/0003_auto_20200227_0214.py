# Generated by Django 3.0.2 on 2020-02-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200222_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity_with_unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]