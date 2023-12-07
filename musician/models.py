from django.db import models

class Musician(models.Model) :
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=14)
    instrument_type = models.CharField(max_length=50)

    def __str__(self) :
        return f"{self.firstName} {self.lastName}"