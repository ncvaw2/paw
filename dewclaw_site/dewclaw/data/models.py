from django.db import models

# Create your models here.
from django.db import models
from adaptor.model import CsvDbModel
from django.core.validators import RegexValidator

CODE_MALE='M'
CODE_FEMALE='F'

CHOICES_GENDER = (
    (CODE_MALE, 'Male'),
    (CODE_FEMALE, 'Female'),
#this is for creating text: his, her, him, etc.
)


CHOICES_PARTY = (
    ('DEM', 'Democratic'),
    ('REP', 'Republican'),
    ('IND', 'Independent'),
    ('LIB', 'Libertarian'),
#this is for creating text: his, her, him, etc.
)

class Person(models.Model):
    key_name = models.CharField(max_length=40, unique=True) #lastname.firstname must be unique, lowercase, for URLs
    name_first = models.CharField(max_length=40,blank=True)
    name_last = models.CharField(max_length=40,blank=True)
    name_full =  models.CharField(max_length=200,blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER,default=CODE_MALE)
    party =  models.CharField(max_length=1, choices=CHOICES_PARTY,default='REP')
    grade_override= models.CharField(max_length=4,blank=True)
    addr = models.CharField(max_length=40,blank=True)
    city = models.CharField(max_length=40,blank=True)
    state = models.CharField(max_length=40,blank=True)
    zip = models.CharField(max_length=40,blank=True)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        #validators=[phone_regex],
        blank=True,max_length=40) # validators should be a list

    def __str__(self):  # __unicode__ on Python 2
        return self.name_full
    #admin stuff
    import_id_fields=['key_name']
    list_display  = ('key_name', 'name_full')

class Issue(models.Model):
    text_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200, default="add desc here")
    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Session(models.Model):
    year = models.SlugField(max_length=30)  # eg: 2015 using text instead of number to allow for special sessions.
    range = models.CharField(max_length=30)  # eg: 2015-2016 using text instead of number to allow for special sessions.
    ncleg_id = models.CharField(max_length=30)  # eg: 2015       #ID on ncleg.net website
    def __str__(self):
        return self.range

class Bill(models.Model):
    session = models.ForeignKey(Session)
    doc_name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.session.year + " " + self.doc_name


CODE_SENATE='S'
CODE_HOUSE='H'
CHOICES_BRANCH = (
    (CODE_SENATE, 'Senate'),
    (CODE_HOUSE, 'House'),
   # ('J', 'Judges'),
)
class Branch(models.Model):
     name = models.CharField(max_length=30)


class District(models.Model):
    branch = models.CharField(max_length=1, choices=CHOICES_BRANCH,default=CODE_HOUSE)  # S= senate H = house
    number = models.DecimalField( max_digits=5,decimal_places=0)
    version = models.DecimalField( max_digits=5,decimal_places=0) # Year district maps went into effect: 2011
    counties = models.CharField(max_length=200)  #  comma seperated counties, create index?
    def __str__(self):  # __unicode__ on Python 2
        return self.branch + " " + str(self.number) + " " + self.counties


class DistrictCsv(CsvDbModel):
     class Meta:
        dbModel = District
        delimiter = ","


class Office(models.Model):
    branch_code = models.CharField(max_length=1, choices=CHOICES_BRANCH,default=CODE_HOUSE)  # S= senate H = house
    dist = models.ForeignKey(District)
    def __str__(self):  # __unicode__ on Python 2
        return self.branch_code + " " + str(self.dist)

class OfficeFill(models.Model):
    office = models.ForeignKey(Office)
    person = models.ForeignKey(Person)
    session = models.ForeignKey(Session)

    def __str__(self):  # __unicode__ on Python 2
        # return  #self.office.dist+" "+
        #return self.office+" "+self.person
        return self.person


class Election(models.Model):
    year = models.DecimalField( max_digits=6,decimal_places=0)

class Candidate(models.Model):
    person = models.ForeignKey(Person)
    office = models.ForeignKey(Office)
    office = models.ForeignKey(Election)

