# Generated by Django 3.1 on 2020-08-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0024_auto_20200826_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]