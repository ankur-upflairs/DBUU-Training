from django.db import models

# Create your models here.

class Courses(models.Model):
    title=models.CharField()
    
    def __str__(self):
        return f"<id ({self.id}) title={self.title}>"



