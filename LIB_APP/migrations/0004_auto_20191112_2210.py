# Generated by Django 2.2.6 on 2019-11-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LIB_APP', '0003_auto_20191112_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='redaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LIB_APP.Redaction'),
        ),
    ]
