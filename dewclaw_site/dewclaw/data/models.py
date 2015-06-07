from django.db import models

# Create your models here.
from django.db import models


class Issue(models.Model):
    text_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200, default="add desc here")


class Session(models.Model):
    year = models.CharField(max_length=30)  # eg: 2015 using text instead of number to allow for special sessions.
    range = models.CharField(max_length=30)  # eg: 2015-2016 using text instead of number to allow for special sessions.
    ncleg_id = models.CharField(max_length=30)  # eg: 2015       #ID on ncleg.net website


class Bill(models.Model):
    session = models.ForeignKey(Session)
    doc_name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.session.year + " " + self.doc_name


class Branch(models.Model):
    name = "Senate"  # custom field??


class District(models.Model):
    branch_code = models.CharField(max_length=1)  # S= senate H = house
    number = models.DecimalField( max_digits=5,decimal_places=0)


class Office(models.Model):
    branch_code = models.CharField(max_length=1)  # S= senate H = house
    dist = models.ForeignKey(District)

class OfficeFill(models.Model):
    dist = models.ForeignKey(Office)





class Person(models.Model):
    name_first = models.CharField(max_length=40)
    name_last = models.CharField(max_length=40)
