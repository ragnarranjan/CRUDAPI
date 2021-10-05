from django.db import models

class Bio(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Colleage = models.CharField(max_length=20)
    Branch = models.CharField(max_length=20)
    Address = models.CharField(max_length=40)
    Roll = models.IntegerField()

    def __str__(self):
        return self.Name

