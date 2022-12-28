from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from obtenerIP.views import views1
from obtenerIP.views import views2
from obtenerIP.views import views3
from obtenerIP.views import views4
from obtenerIP.views import views5

urlpatterns = [
    
    path('obtenerIP/', views1.EncontrarUbicacion1.as_view()),
    path('obtenerIP2/', views2.EncontrarUbicacion2.as_view()),
    path('obtenerIP3/', views3.EncontrarUbicacion3.as_view()),
    path('obtenerIP4/', views4.EncontrarUbicacion4.as_view()),
    path('obtenerIP5/', views5.EncontrarUbicacion5.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)