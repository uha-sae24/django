from django.urls import  path
from . import views 

urlpatterns = [
    path("",views.index,name="index"),
    path('purge/', views.purge, name='purge'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('all_data/', views.all_data, name='all_data'),
    path('sensor_data/<str:sensor_id>/', views.sensor_data, name='sensor_data'),
    path('edit_sensor/<str:sensor_id>/', views.edit_sensor, name='edit_sensor'),
]
