# Generated by Django 4.2.7 on 2023-11-17 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]