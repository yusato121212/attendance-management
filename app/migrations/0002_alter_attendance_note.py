# Generated by Django 3.2.8 on 2021-11-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='note',
            field=models.CharField(default='', max_length=50, verbose_name='備考'),
        ),
    ]
