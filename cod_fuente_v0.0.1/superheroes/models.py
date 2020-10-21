from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    founder = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name',]

class SuperHeroe(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')
    real_name = models.CharField(max_length=100, blank=True, default='')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']