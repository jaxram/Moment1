# Generated by Django 3.1.1 on 2021-02-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mectworkplace', '0012_auto_20210204_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='hostel_room',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
