# Generated by Django 3.1.3 on 2021-03-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210321_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='volunteer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
