# Generated by Django 3.2.3 on 2021-05-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]