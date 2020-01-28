from django.db import models

# Create your models here.
''' name, price, quantity, status , date , description '''

class Erp(models.Model):

    name = models.CharField(max_length=100, unique=True, 
    error_messages={
        "unique" : "this name already exist"
    }
    )
    email = models.EmailField()
    ph = models.CharField(max_length=100)
    date = models.DateTimeField()
    gender = models.CharField(max_length=10)
    experience = models.IntegerField(default=0)
    hospital_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=100)



    

    def __str__(self):
        return self.name
