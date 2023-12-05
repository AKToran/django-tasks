from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, help_text="enter your name") 
    roll = models.AutoField(primary_key=True)
    email = models.EmailField()
    address = models.TextField(help_text="Enter address")
    father_name = models.CharField(max_length=20)
    big_integer_field = models.BigIntegerField()
    passed = models.BooleanField(help_text="did you pass the exam?")
    enroll_date = models.DateField()
    absent = models.DateTimeField(default=datetime.datetime.now())
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    float_field = models.FloatField()



    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"
    