# Generated by Django 3.1 on 2020-08-20 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0002_auto_20200820_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='church',
            name='former_religion',
        ),
    ]
