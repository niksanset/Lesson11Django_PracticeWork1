# Generated by Django 4.2.7 on 2023-11-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_student_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
