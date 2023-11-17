from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify



class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=255)
    music_instrumet = models.CharField(max_length=255)
    grade = models.IntegerField()
    pay_or_not = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            blank=True,
                            unique=True)

    
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.first_name}-{self.last_name}")
        return super().save()

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.age}"
