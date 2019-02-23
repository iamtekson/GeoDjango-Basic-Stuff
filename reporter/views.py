from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Incidences, Districts

def index(request):
	return render(request, 'pages/index.html')

def district_datasets(request):
	districts = serialize('geojson', Districts.objects.all())
	return HttpResponse(districts, content_type='json')

def point_datasets(request):
	districts = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points, content_type='json')	