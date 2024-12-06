from django.db import models


# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=20)
    yob = models.DateField()

    def __str__(self):
        return self.fullname

class Member(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Bookings(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100,)
    occupation = models.CharField(max_length=255,)
    rating = models.IntegerField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name
