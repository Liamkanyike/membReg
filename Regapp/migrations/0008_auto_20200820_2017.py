# Generated by Django 3.1 on 2020-08-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0007_auto_20200820_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='baptised',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='born_again',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='marital_status',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='photo',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='spirit_filled',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
