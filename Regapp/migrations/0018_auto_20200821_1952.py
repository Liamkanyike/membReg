# Generated by Django 3.1 on 2020-08-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0017_church_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='registration_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
