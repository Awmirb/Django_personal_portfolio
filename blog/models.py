from django.db import models

class blogs(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
