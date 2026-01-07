from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{10,15}$',
    message="Enter a valid contact number (10–15 digits)"
)

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=100,null=False,blank=False)
    contact_num = models.CharField(max_length=15,validators=[phone_validator],null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='photos/',null=True,blank=True)
    admission_date = models.DateField()
    course = models.CharField(max_length=50,null=False,blank=False)
    course_description = models.TextField()

    def __str__(self):
        return self.name