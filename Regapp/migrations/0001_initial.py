# Generated by Django 3.1 on 2020-08-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('residential_address', models.CharField(max_length=25, null=True)),
                ('former_religion', models.CharField(max_length=25, null=True)),
                ('name_of_church', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
