from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader

# Import data
from dashboard.models import Relics
from dashboard.forms import RelicsForm

# Import forms
from dashboard.forms import RelicsForm

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
    # template = loader.get_template('relics.html')
    
    if request.GET.__contains__('relics_filter'):
        relics_data = Relics.objects.values().filter(mod_type=request.GET['relics_filter'])
    else:
        print("Outside")
        relics_data = Relics.objects.all().values()

    mod_types = Relics.objects.values('mod_type').distinct()

    context={
        'Relics': relics_data,
        'Mod_types': mod_types,
        }
    
    return render(request, "relics.html", context=context)
    
    # return HttpResponse(template.render(context, request))