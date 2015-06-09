# Register your models here.
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from import_export.admin import ImportExportModelAdmin,ExportMixin
from import_export import fields,widgets
from import_export import resources



from .models import *


class IssueResource(resources.ModelResource):
    class Meta:
        model = Issue

class IssueAdmin(ImportExportModelAdmin):
    resource_class = IssueResource
    pass

admin.site.register(Issue, IssueAdmin)
admin.site.register([Session,Bill,Branch,District,Office ,Person])
