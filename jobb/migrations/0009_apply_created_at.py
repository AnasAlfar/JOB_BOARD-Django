# Generated by Django 4.2.6 on 2023-10-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobb', '0008_apply_delete_aplly'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
