# Generated by Django 3.2.22 on 2024-01-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmaster',
            name='VAT',
            field=models.CharField(max_length=50),
        ),
    ]
