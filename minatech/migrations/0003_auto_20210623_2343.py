# Generated by Django 3.0.6 on 2021-06-23 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minatech', '0002_auto_20210623_2330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='courses',
        ),
    ]