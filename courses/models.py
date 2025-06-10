from django.db import models

class Course(models.Model):
    AGE_GROUPS = [
        ('kids', 'Малышам'),
        ('school', 'Школьникам'),
    ]

    title = models.CharField(max_length=255)
    age = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)  # например: "6 месяцев"
    lesson_time = models.CharField(max_length=50)  # например: "30 минут"
    description = models.TextField()
    age_group = models.CharField(max_length=10, choices=AGE_GROUPS)
    image_url = models.URLField(blank=True)  
    program = models.JSONField(default=list)  # список тем курса
    price = models.IntegerField(default=0)    # цена в рублях

    def __str__(self):
        return self.title


