from django.urls import  path
from . import views 

urlpatterns = [
    path("",views.main),
    path('name_update_A/<str:id>/',views.name_update_A, name='name_update_A'),
    path('name_update_B/<str:id>/',views.name_update_B,name='name_update_B'),
    path('purge/', views.purge, name='purge'),
    path('updatetraitement/<str:id>/',views.updatetraitement,name='updatetraitement'),
    path('affichage_spe/',views.affichage_spe,name='affichage_spe'),
    path('valeurCapteur/',views.focus,name='focus'),
    path('export_csv/', views.export_csv, name='export_csv'),
    #path('affichage_spe/<str:id>/', views.affichage_spe_id),
    #path('affichage_spe/<str:id>/<')
    path('capteur/<str:id>/', views.capteur_data, name='capteur_data'),
]
