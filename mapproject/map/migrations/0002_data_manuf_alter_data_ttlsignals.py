# Generated by Django 4.0.1 on 2022-01-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='manuf',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='ttlsignals',
            field=models.IntegerField(default=0),
        ),
    ]
