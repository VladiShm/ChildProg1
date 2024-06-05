from django.db import models


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

    def __str__(self):
        return f'Практическая задача для теории: {self.theory.title}'