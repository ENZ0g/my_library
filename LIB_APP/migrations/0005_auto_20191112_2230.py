# Generated by Django 2.2.6 on 2019-11-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIB_APP', '0004_auto_20191112_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(error_messages={'max_length': 'Только 2 буквы'}, max_length=2),
        ),
    ]
