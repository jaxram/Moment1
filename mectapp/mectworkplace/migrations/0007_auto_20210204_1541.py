# Generated by Django 3.1.1 on 2021-02-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mectworkplace', '0006_certificate_studentdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='userid',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]