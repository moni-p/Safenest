# Generated by Django 3.1.3 on 2021-03-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210325_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
