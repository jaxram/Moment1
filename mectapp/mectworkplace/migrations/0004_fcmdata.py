# Generated by Django 3.1.1 on 2022-01-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mectworkplace', '0003_delete_fcmdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='fcmdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('fcmtoken', models.CharField(max_length=200, null=True)),
                ('topics_subscribed', models.CharField(max_length=100, null=True)),
                ('time_sub', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]