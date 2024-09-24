from django.db import models

class FavCars(models.Model):
    fav_image=models.TextField(max_length=100)
    fav_name=models.TextField(max_length=200)
    fav_desc=models.TextField(max_length=200)
    def __str__(self):
        return self.fav_image
class Department(models.Model):
    fav_image=models.ForeignKey(FavCars, models.CASCADE)
    dep_price=models.TextField(max_length=200)
    def __str__(self):
        return self.dep_price
class Contact(models.Model):
    name=models.TextField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    message=models.TextField(max_length=200)
    def __str__(self):
        return self.name