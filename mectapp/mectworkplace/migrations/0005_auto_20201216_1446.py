# Generated by Django 3.1.1 on 2020-12-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mectworkplace', '0004_auto_20201216_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='td',
            name='student',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]