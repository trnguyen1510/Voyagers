# Generated by Django 3.1.2 on 2020-10-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0004_auto_20201027_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
