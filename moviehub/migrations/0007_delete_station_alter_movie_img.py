# Generated by Django 4.2 on 2024-07-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviehub', '0006_remove_station_code_station_waiting_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='movies/default.webp', upload_to='gallery'),
        ),
    ]
