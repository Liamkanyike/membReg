# Generated by Django 3.1 on 2020-08-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0005_church_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='birthday',
            field=models.CharField(max_length=30, null=True),
        ),
    ]