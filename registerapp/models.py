from django.db import models
from django.core.exceptions import ValidationError 

# Create your models here.
def validate_passward(value): 
    if len(value)>=8: 
        return value 
    else: 
        raise ValidationError("passward must be 8 char")

def validate_phone(value): 
    if len(str(value))==10: 
        return value 
    else: 
        raise ValidationError("phone must be 10 digit")

def validate_name(value): 
    a=False
    for x in value:
        if ord("a")<=ord(x)<=ord("z") or ord("A")<=ord(x)<=ord("Z"):
            a=True
        else:
            a=False
            break
    if a:
        return value
    else:
        raise ValidationError(" alphabate only")
    

 

class User(models.Model):
    name=models.CharField(max_length=30,validators=[validate_name])
    userid=models.CharField(max_length=20)
    email=models.EmailField()
    phone_no=models.IntegerField(validators=[validate_phone])
    passward=models.CharField(max_length=20,validators=[validate_passward])
    retype_passward=models.CharField(max_length=20)

    

    def __str__(self):
        return self.userid