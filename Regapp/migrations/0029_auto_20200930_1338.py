# Generated by Django 3.1.1 on 2020-09-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0028_auto_20200930_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='church',
            name='scanned_document',
            field=models.FileField(blank=True, max_length=25, null=True, upload_to='scanned_documents'),
        ),
    ]