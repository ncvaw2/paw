from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register([Issue,Session,Bill,Branch,District,Office ,Person])

