# Generated by Django 2.2.5 on 2019-11-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191112_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrovehiculos',
            name='patente',
        ),
        migrations.AlterField(
            model_name='registrovehiculos',
            name='vehiculo',
            field=models.CharField(max_length=7),
        ),
    ]
