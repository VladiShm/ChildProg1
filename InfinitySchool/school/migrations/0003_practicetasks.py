# Generated by Django 5.0.6 on 2024-06-04 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_coursestheory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('difficulty', models.CharField(max_length=50)),
                ('theory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='school.coursestheory')),
            ],
        ),
    ]
