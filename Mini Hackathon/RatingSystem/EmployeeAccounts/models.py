from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class EmployeeAccounts(models.Model):
    Name = models.CharField(null=False, blank=False,max_length=30)
    Email = models.EmailField(max_length = 100)
    #EmployeeID = models.IntegerField()
    password = models.CharField(max_length=50)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
    def __str__(self):
        return self.Name