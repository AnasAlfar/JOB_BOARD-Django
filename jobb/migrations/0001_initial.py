# Generated by Django 4.2.6 on 2023-10-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15)),
            ],
        ),
    ]
