from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Courses(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='courses_images')

    def __str__(self):
        return f'Курс: {self.name}'


class CoursesTheory(models.Model):
    course = models.ForeignKey(Courses, related_name='theories', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    theory = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title} для курса: {self.course.name}'


class PracticeTasks(models.Model):
    theory = models.ForeignKey(CoursesTheory, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Практическая задача для теории: {self.theory.title}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)