from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, help_text="enter your name", default=None) 
    roll = models.AutoField(primary_key=True, default=None)
    email = models.EmailField(default=None)
    address = models.TextField(help_text="Enter address", default=None)
    father_name = models.CharField(max_length=20, default=None)
    big_integer_field = models.BigIntegerField(default=None)
    passed = models.BooleanField(help_text="did you pass the exam?", default=None)
    enroll_date = models.DateField(default=None)
    absent = models.DateTimeField(default=datetime.datetime.now())
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=None)
    duration_field = models.DurationField( default=None)
    file_field = models.FileField(upload_to='files/', default=None)
    float_field = models.FloatField( default=None)
    image_field = models.ImageField(upload_to='images/', default=None)
    


    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"
    