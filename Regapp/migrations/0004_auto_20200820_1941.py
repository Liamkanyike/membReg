# Generated by Django 3.1 on 2020-08-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0003_remove_church_former_religion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='church',
            name='name_of_church',
        ),
        migrations.AddField(
            model_name='church',
            name='former_religion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='postal_address',
            field=models.CharField(max_length=25, null=True),
        ),
    ]