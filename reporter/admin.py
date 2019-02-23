#from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Incidences, Districts
from leaflet.admin import LeafletGeoAdmin

#class IncidencesAdmin(admin.ModelAdmin):
	#list_display = ('name', 'location')

class IncidencesAdmin(LeafletGeoAdmin):
	list_display = ('name', 'location')

class DistrictsAdmin(LeafletGeoAdmin):
	list_display = ('objectid', 'dist_name')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Districts, DistrictsAdmin)


