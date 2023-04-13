from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    release_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'