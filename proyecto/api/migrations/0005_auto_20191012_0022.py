# Generated by Django 2.2.5 on 2019-10-12 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190913_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrovehiculos',
            name='day',
        ),
        migrations.RemoveField(
            model_name='registrovehiculos',
            name='month',
        ),
        migrations.RemoveField(
            model_name='registrovehiculos',
            name='year',
        ),
        migrations.AddField(
            model_name='registrovehiculos',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
