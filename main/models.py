from django.db import models


class Translator(models.Model):
    src = models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    text = models.CharField(max_length=255)


class Lang(models.Model):
    name = models.CharField(max_length=100)
    c_code = models.CharField(max_length=10)
    l_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
