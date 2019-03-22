from django.db import models

class fdata(models.Model):
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class questions(models.Model):
    fq1 = models.CharField( default = "Clarity About the Topic ", max_length = 1000)
    fq2 = models.CharField( default = "Regularity And Punctuality of the Faculty ",max_length = 1000)
    fq3 = models.CharField(default = "Pace Of Teaching ",max_length = 1000)
    topic1 = models.CharField(default = "",max_length = 1000 , blank = True)
    topic2 = models.CharField(default = "",max_length = 1000 , blank = True)
    topic3 = models.CharField(default = "",max_length = 1000 , blank = True)
    topic4 = models.CharField(default = "",max_length = 1000 , blank = True)
    topic5 = models.CharField(default = "",max_length = 1000 , blank = True)
