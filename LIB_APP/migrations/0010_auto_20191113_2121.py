# Generated by Django 2.2.6 on 2019-11-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIB_APP', '0009_auto_20191113_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookholder',
            name='birth_date',
            field=models.DateField(),
        ),
    ]