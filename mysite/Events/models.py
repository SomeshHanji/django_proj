from django.db import models


# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip/Post code', max_length=12)
    phone = models.CharField('contact phone', max_length=20,blank=True)
    web = models.URLField('Web Address',blank=True)
    email_address = models.EmailField('Email Address',blank=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField("Events", max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(' user Email')
    def __str__(self):
        return self.first_name + " " + self.first_name
