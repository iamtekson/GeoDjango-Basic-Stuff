from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name= 'index'),
	path('districts/', views.district_datasets, name='districts'),
	path('incidence_data/', views.point_datasets, name='incidences'),
]