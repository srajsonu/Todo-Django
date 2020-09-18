from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=256)

class Task(models.Model): #table
    content = models.TextField() #column
    deadline = models.DateTimeField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    class TaskStatus(models.TextChoices):
        COMPLETED = "CO", "Completed"
        PENDING = "PE", "Pending"
        DROPPED = "DR", "Dropped"

    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2
    )






