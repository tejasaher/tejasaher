# Generated by Django 3.1.3 on 2021-02-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geo_code',
            name='seo_id',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
