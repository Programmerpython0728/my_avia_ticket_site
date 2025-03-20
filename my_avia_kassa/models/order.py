from  django.db import models
from .product import Ticket
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User=get_user_model()

phone_regex=RegexValidator(regex=r'^\+998\d{9}$',
                           message="Telefon raqam shu shakilda bolishi kerak +998xxxxxxxxx")

class Order(models.Model):
    SOTIB_OLINDI='Sotib olindi'
    SOTIB_OLINMADI='Sotib olinmadi'

    STATUS_CHOICES=[
        (SOTIB_OLINDI,'Sotib olindi'),
        (SOTIB_OLINMADI,'Sotib olinmadi')

    ]
    product=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=SOTIB_OLINMADI)
    phone_number=models.CharField(validators=[phone_regex],max_length=13,blank=True,null=True)
    is_paid=models.BooleanField(default=True,null=False)
    quantity=models.IntegerField(default=1)

    def set_status(self,new_status):
        if new_status not in dict(self.STATUS_CHOICES):
            raise ValueError("Invalid Status")
        self.status=new_status
        self.save()

    def __str__(self):
        return f"Order({self.product} by {self.customer})"

