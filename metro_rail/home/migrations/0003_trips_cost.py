# Generated by Django 4.1.7 on 2023-03-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='cost',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
