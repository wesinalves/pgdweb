# Generated by Django 3.1.1 on 2021-01-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0005_auto_20210119_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateTimeField(verbose_name='Data Nascimento'),
        ),
    ]
