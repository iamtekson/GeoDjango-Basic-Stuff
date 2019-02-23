from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
 
class Incidences(models.Model):
	name = models.CharField(max_length=30)
	location = models.PointField(srid=4326)
	#objects = models.GeoManager()

	def __str__(self):
		return self.name

class Districts(models.Model):
    objectid = models.IntegerField()
    dcode = models.IntegerField()
    dist_name = models.CharField(max_length=18)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    code1 = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
    	return self.objectid()