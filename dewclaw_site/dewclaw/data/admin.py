# Register your models here.
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from import_export.admin import ImportExportModelAdmin,ExportMixin
from import_export import fields,widgets
from import_export import resources



from .models import *

class GenAdmin(ImportExportModelAdmin):
    #resource_class = IssueResource
    pass

#TODO - there as to be a generic way to define these classes

# Register your models here.
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from import_export.admin import ImportExportModelAdmin,ExportMixin
from import_export import fields,widgets
from import_export import resources
import data.models as data_models


from .models import *
#
# class resPerson(resources.ModelResource):
#     class Meta:
#         model = Person
#         import_id_fields=['key_name']
#
# class admPerson(ImportExportModelAdmin):
#     list_display  = ('key_name', 'name_full')
#     resource_class=resPerson
#     pass

#admin.site.register(Person,admPerson)

def get_class_res(cl):
    res_cl= type('res'+type(cl).__name__,(resources.ModelResource,),dict(
       Meta=type('Meta',(),dict(model=cl))))
    if hasattr(cl,'import_id_fields'):
        res_cl.import_id_fields=cl.import_id_fields
    return res_cl

def get_class_admin(cl):
    adm_cl=type('admin'+type(cl).__name__,(ImportExportModelAdmin,),dict(
        resource_class=get_class_res(cl)))
    adm_cl.list_display= [x.name for x in cl._meta.local_fields]
    return adm_cl

def register_admins(set):
    for cl in set:
        admin.site.register(cl, get_class_admin(cl))




register_admins([Session,Bill,Branch,Office,District,Person,Issue,OfficeFill])



