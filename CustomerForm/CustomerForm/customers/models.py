from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField("Họ và tên", max_length=100)
    telephone = models.CharField("Số điện thoại", max_length=20)
    address = models.CharField("Địa chỉ", max_length=200)
    email = models.EmailField(primary_key=True)
    nenkin_1_status = models.CharField("Nenkin 1", max_length=200)
    nenkin_2_status = models.CharField("Nenkin 2", max_length=200)

    def __str__(self):
        return self.name