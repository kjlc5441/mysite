# Generated by Django 2.2.12 on 2021-10-17 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flag',
            options={'verbose_name': '燈號', 'verbose_name_plural': '燈號'},
        ),
        migrations.AlterModelTable(
            name='flag',
            table='flag',
        ),
    ]
