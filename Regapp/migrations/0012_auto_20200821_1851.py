# Generated by Django 3.1 on 2020-08-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0011_auto_20200821_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='alive_parents',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='church_county',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='church_district',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='church_lc1',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='church_lc2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='church_lc3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='church_police',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='membership_size',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='name_of_church',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='parents_names',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]