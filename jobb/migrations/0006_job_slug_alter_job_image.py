# Generated by Django 4.2.6 on 2023-10-21 20:15

from django.db import migrations, models
import jobb.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobb', '0005_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=jobb.models.image_upload),
        ),
    ]