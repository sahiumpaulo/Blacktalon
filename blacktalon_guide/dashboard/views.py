from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader

# Import data
from dashboard.models import Relics

def dashboard_with_pivot(request):
    template = loader.get_template('dashboard_with_pivot.html')
    # relics_data = Relics.objects.all()
    # context={'Relics': relics_data}
    context = {}
    return HttpResponse(template.render(context, request))

def pivot_data(request):
    dataset = Relics.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def relics_data(request):
    template = loader.get_template('relics.html')
    relics_data = Relics.objects.all().values()
    
    context={
        'Relics': relics_data
        }
    
    return HttpResponse(template.render(context, request))