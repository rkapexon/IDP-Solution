from django.db import models

# Create your models here.
 
# Create your models here.
 
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
 
class CustomerInfo(models.Model):
    full_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    country_code = models.CharField(max_length=3)
    phone_number = PhoneNumberField(max_length=15)
    account_number = models.CharField(max_length=15)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.full_name
 
class mydb(models.Model):
    id = models.AutoField(primary_key=True)
    formid = models.CharField(max_length=50)
    apiVersion = models.CharField(max_length=50)
    modelId = models.CharField(max_length=50)
    field_name = models.CharField(max_length=100)
    OCR_value = models.CharField(max_length=255)
    Edited_value = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    
    class Meta:
        db_table = 'ds_ocr_exp'