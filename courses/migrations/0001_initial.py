# Generated by Django 5.2.1 on 2025-05-22 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('lesson_time', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('age_group', models.CharField(choices=[('kids', 'Малышам'), ('school', 'Школьникам')], max_length=10)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
    ]
