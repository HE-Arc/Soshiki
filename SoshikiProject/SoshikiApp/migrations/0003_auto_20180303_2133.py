# Generated by Django 2.0.2 on 2018-03-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoshikiApp', '0002_auto_20180303_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deadline',
            field=models.DateTimeField(verbose_name='Deadline'),
        ),
    ]
