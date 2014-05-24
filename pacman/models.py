from django.db import models

class Distribution(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    active      = models.BooleanField()
    url         = models.TextField()

    def __str__(self):
        return self.name

class Mirror(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    active      = models.BooleanField()

    def __str__(self):
        return self.name

class Mirror_Distribution(models.Model):
    mirror       = models.ForeignKey('Mirror')
    distribution = models.ForeignKey('Distribution')

    def __str__(self):
        return self.mirror.name + " - " +  self.distribution.name
