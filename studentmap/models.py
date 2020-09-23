from django.db import models

# Create your models here.


class StudentLocation(models.Model):

    id = models.AutoField(primary_key=True)
    stud_id = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    stud_name = models.CharField(max_length=50)
    stud_age = models.IntegerField(max_length=50)
    stud_pnumber = models.CharField(max_length=50)
    stud_course = models.CharField(max_length=50)
    stud_year = models.CharField(max_length=50)
    hlat = models.DecimalField(max_digits=10, decimal_places=6)
    hlong = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        self.stud_id
