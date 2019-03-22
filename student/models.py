from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class sdata(models.Model):
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    dept = models.CharField(max_length = 100)
    rid = models.IntegerField()
    email = models.CharField(max_length = 100)
    phone = models.IntegerField(validators = [ MinValueValidator(1000000000) , MaxValueValidator(9999999999)])

    def __str__(self):
        return self.name + " - " + str(self.rid)

class submissiondata(models.Model):
    q1 = models.IntegerField(default = 3,validators = [ MinValueValidator(0) , MaxValueValidator(5)])
    q2 = models.IntegerField(default = 3,validators = [ MinValueValidator(0) , MaxValueValidator(5)])
    q3 = models.IntegerField(default = 3,validators = [ MinValueValidator(0) , MaxValueValidator(5)])
    q4 = models.CharField(default = "" , max_length = 1000)
    q5 = models.IntegerField(default = 0, validators = [ MinValueValidator(-1) , MaxValueValidator(1)])
    q5text = models.CharField(default = "" , max_length = 1000)
