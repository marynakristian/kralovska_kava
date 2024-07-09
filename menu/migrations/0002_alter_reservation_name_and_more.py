# Generated by Django 5.0.7 on 2024-07-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_people',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
