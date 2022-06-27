from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=255, default='Ravshan')
    age = models.IntegerField(default=998)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name



