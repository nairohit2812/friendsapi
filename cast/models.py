from django.db import models

class Cast(models.Model):
    name = models.CharField(max_length=50)
    character  = models.CharField(max_length=50)
    oneliner = models.CharField(max_length=500)
    episode = models.CharField(max_length=50)

    def __str__(self):
        return self.name