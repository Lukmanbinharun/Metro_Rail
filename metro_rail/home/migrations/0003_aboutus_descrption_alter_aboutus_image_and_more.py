# Generated by Django 4.1.5 on 2023-03-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_aboutus_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='descrption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(upload_to='./static/images'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]