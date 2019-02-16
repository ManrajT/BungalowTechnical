from django.shortcuts import render
from django.views import generic 
from bungalow.models import Property
from django.http import JsonResponse 
import json
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'bungalow/index.html'

    def get_queryset(self):
        return "" 

#This method will return all property as json
def getAllData(request):
    all_property_objects = Property.objects.all().values()
    return JsonResponse({"all_property_objects": list(all_property_objects)})



