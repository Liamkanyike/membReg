# Generated by Django 3.1 on 2020-08-20 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0004_auto_20200820_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
