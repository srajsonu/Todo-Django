from django.db import models

# Create your models here.
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Task(models.Model): #table
    content = models.TextField() #column
    created_at = models.DateTimeField(
        default=timezone.now()
    )
    deadline = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    class TaskStatus(models.TextChoices):
        COMPLETED = "CO", "Completed"
        PENDING = "PE", "Pending"
        DROPPED = "DR", "Dropped"

    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2
    )

    def __str__(self):
        return self.content








