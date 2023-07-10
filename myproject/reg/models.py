from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    phone_number = models.BigIntegerField(unique=True)
    job_id = models.CharField(max_length=45)
    salary = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'employee'
