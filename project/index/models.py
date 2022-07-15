from django.db import models
from django.urls import reverse


class Main(models.Model):
    name = models.CharField(max_length=255, default='Ravshan', null=True)
    age = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    img = models.ImageField(upload_to='backend_images/main_table', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bu mening main jadvalim'


class MainId(models.Model):
    main_id = models.ForeignKey(Main, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.gender

    def get_absolute_url(self):
        return reverse('sec', kwargs={'raqam': self.slug})

    class Meta:
        verbose_name_plural = 'Bu mening mainId jadvalim'




