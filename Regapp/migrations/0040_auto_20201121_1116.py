# Generated by Django 3.1.3 on 2020-11-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0039_auto_20201121_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='church',
            old_name='children',
            new_name='any_children',
        ),
        migrations.AddField(
            model_name='church',
            name='number_of_children',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
