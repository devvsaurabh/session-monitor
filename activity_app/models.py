from django.db import models

# Create your models here.
class User(models.Model):
    c_id = models.CharField(max_length=20,unique=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    c_id = models.CharField(max_length=20)
    start_time= models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.start_time)
