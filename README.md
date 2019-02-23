# GeoDjango-basic-tutorial
>> pip install django <br/>
>> pip install psycopg2 <br/>
>> pip install psycopg2-binary <br/>
>> pip install django.leaflet <br/>

# Basic commands used in GeoDjango

#for displaying shapfiles <br/>
>> python manage.py ogrinspect reporter/data/Districts.shp Districts --srid=4326 --mapping --multi <br/>

# issues occurs in GeoDjango
1. There is no GeoManner model aviable for django 2.0 <br/>
2. Add some program line in setting.py file: <br/>


 import os
	if os.name == 'nt':
    import platform
    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH'] <br/> <br/>
    
    
<h5> The full course link is aviable <a href= 'https://www.youtube.com/watch?v=QiLO3MQxvds&list=PL7amXK4vKqATa_KrfQ3_tEF_ywAgAqWeJ'> HERE</a> </h5>

