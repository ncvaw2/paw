from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
import data.models as data_models

import inspect


def get_tables():
    clsmembers = inspect.getmembers(data_models, inspect.isclass)

    return clsmembers


def index(request):
    tablelist = []
    for table in get_tables():
        tablelist.append(table[0])

    template = loader.get_template('data/index.html')
    context = RequestContext(request, {
        'tablelist': tablelist,
    })
    return HttpResponse(template.render(context))


def get_table(table_name):
    table_list = get_tables()
    table = []
    fields = []

    if table_name in dict(table_list).keys():
        val = dict(table_list)[table_name]
    else:
        val = False

    return val



def table_generic(request, table_name):
    table_cl = get_table(table_name)
    table = []
    fields = []
    if (inspect.isclass(table_cl)):
        msg = "found it!"
        fields=table_cl._meta.fields
        objlist=table_cl.objects.all()

        for obj in objlist:
            row = []
            for f in fields:
                data=getattr(obj,f.name)
                row.append(data)
            table.append(row)



    else:
        msg = "not found"



    template = loader.get_template('data/table.html')
    context = RequestContext(request, {
        'msg': msg,
        'fields': fields,
        'table': table,
        'table_name': table_name,

    })
    return HttpResponse(template.render(context))
