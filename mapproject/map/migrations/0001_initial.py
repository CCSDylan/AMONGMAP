# Generated by Django 4.0.1 on 2022-01-20 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('lat', models.FloatField(default=0)),
                ('long', models.FloatField(default=0)),
                ('ttlsignals', models.FloatField(default=0)),
            ],
        ),
    ]
