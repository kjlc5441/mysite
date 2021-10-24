# Generated by Django 2.2.12 on 2021-10-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gbpay', models.CharField(max_length=3, verbose_name='呷霸卡')),
                ('uupay', models.CharField(max_length=3, verbose_name='悠遊卡')),
                ('twpay', models.CharField(max_length=3, verbose_name='台灣pay')),
            ],
        ),
    ]