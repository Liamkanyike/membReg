# Generated by Django 3.1 on 2020-08-21 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0014_remove_church_scanned_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='church',
            name='registration_date',
        ),
    ]
