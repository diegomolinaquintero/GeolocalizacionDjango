from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from obtenerIP.views import views1
from obtenerIP.views import views2
from obtenerIP.views import views3

urlpatterns = [
    
    path('obtenerIP/', views1.EncontrarUbicacion1.as_view()),
    path('obtenerIP2/', views2.EncontrarUbicacion2.as_view()),
    path('obtenerIP3/', views3.EncontrarUbicacion3.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)