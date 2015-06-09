from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    key_name = models.SlugField( unique=True) #lastname.firstname must be unique, lowercase, for URLs
    name_first = models.CharField(max_length=40)
    name_last = models.CharField(max_length=40)

class Issue(models.Model):
    text_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200, default="add desc here")
    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Session(models.Model):
    year = models.CharField(max_length=30)  # eg: 2015 using text instead of number to allow for special sessions.
    range = models.CharField(max_length=30)  # eg: 2015-2016 using text instead of number to allow for special sessions.
    ncleg_id = models.CharField(max_length=30)  # eg: 2015       #ID on ncleg.net website


class Bill(models.Model):
    session = models.ForeignKey(Session)
    doc_name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.session.year + " " + self.doc_name


CODE_SENATE='S'
CODE_HOUSE='S'
CHOICES_BRANCH = (
    (CODE_SENATE, 'Senate'),
    (CODE_HOUSE, 'House'),
   # ('J', 'Judges'),
)
class Branch(models.Model):
     name = models.CharField(max_length=30)


class District(models.Model):
    branch_code = models.CharField(max_length=1, choices=CHOICES_BRANCH)  # S= senate H = house
    number = models.DecimalField( max_digits=5,decimal_places=0)


class Office(models.Model):
    branch_code = models.CharField(max_length=1, choices=CHOICES_BRANCH)  # S= senate H = house
    dist = models.ForeignKey(District)

class OfficeFill(models.Model):
    office = models.ForeignKey(Office)
    person = models.ForeignKey(Person)
    session = models.ForeignKey(Session)

class Election(models.Model):
    year = models.DecimalField( max_digits=6,decimal_places=0)

class Canadate(models.Model):
    person = models.ForeignKey(Person)
    office = models.ForeignKey(Office)
    office = models.ForeignKey(Election)

