# Generated by Django 4.2 on 2024-07-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviehub', '0007_delete_station_alter_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='gallery/default.jpg', upload_to='gallery'),
        ),
    ]
