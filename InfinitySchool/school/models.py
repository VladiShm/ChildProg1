from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='courses_images')

    def __str__(self):
        return f'Курс: {self.name}'