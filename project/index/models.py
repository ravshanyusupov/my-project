from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=255, default='Ravshan')
    age = models.IntegerField(blank=True)
    description = models.TextField(max_length=500, blank=True)
    img = models.ImageField(upload_to='backend_images/main_table', blank=True)

    def __str__(self):
        return self.name

    def desc(self):
        return self.description[:50]


class MainId(models.Model):
    main_id = models.ForeignKey(Main, on_delete=models.CASCADE, related_name='related_name')
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender




