import os
from django.contrib.gis.utils import LayerMapping
from .models import Districts

districts_mapping = {
    'objectid': 'OBJECTID',
    'dcode': 'DCODE',
    'dist_name': 'DIST_NAME',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'code1': 'CODE1',
    'geom': 'MULTIPOLYGON',
}

dist_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/Districts.shp'))

def run(verbase=True):
	lm = LayerMapping(Districts, dist_shp, districts_mapping, transform = False,encoding='iso-8859-1')
	lm.save(strict=True)