# Generated by Django 3.1 on 2020-08-26 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0021_auto_20200822_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
