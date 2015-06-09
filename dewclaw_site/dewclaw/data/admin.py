# Register your models here.
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from import_export.admin import ImportExportModelAdmin,ExportMixin
from import_export import fields,widgets
from import_export import resources



from .models import *


class GenResource(resources.ModelResource):
    name= {}
    def __init__(self, classname):
        name=classname
    def foo(self):
        self.name
    class Meta:
        model = Issue

class GenAdmin(ImportExportModelAdmin):
    #resource_class = IssueResource
    pass

#TODO - there as to be a generic way to define these classes

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District

class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictResource
    pass



class IssueResource(resources.ModelResource):
    class Meta:
        model = Issue

class IssueAdmin(ImportExportModelAdmin):
    resource_class = IssueResource
    pass

admin.site.register(Issue, IssueAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register([Session,Bill,Branch,Office ,Person])
