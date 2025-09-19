from django.db import models
from django.utils import timezone
# Create your models here.

class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    instructor=models.CharField(max_length=50 , blank=True)
    duration=models.IntegerField(null=True)
    createdAt=models.DateField(default=timezone.now)
    updatedAt=models.DateField(auto_now=True)
    image=models.CharField(null=True)
    
    def __str__(self):
        return f"<id ({self.id}) title={self.title}>"



