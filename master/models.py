from django.db import models

# Create your models here.


class ScheduleModel(models.Model):

    PRIORITY_CHOICES = (
        ("5", "High Priority "), 
        ("4", " Middle Priority"),
        ("3", "Moderate Priority"),
        ("2", "Low Priority"),
        ("1", "Emergency"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title


