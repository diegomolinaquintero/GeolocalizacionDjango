from django.http import HttpResponse
from rest_framework.views import APIView
# una api free con contribuciones de este year
from geoip import GeoIP
from geopy.geocoders import Nominatim
#traer email y key para no quemarlos en el codigo
import json
import os
from GeoUbicacion.settings import BASE_DIR


from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
        secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
        """Get secret setting or fail with ImproperlyConfigured"""
        try:
                return secrets[setting]
        except KeyError:
                raise ImproperlyConfigured("Set the {} setting".format(setting))

class EncontrarUbicacion2(APIView):
        def get(self, request):
                #api key gratis de https://surfy.one/geoip
                lookup = GeoIP(get_secret('emailApiSurfy'), get_secret('keyApiSurfy'))
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                        client_ip = x_forwarded_for.split(',')[0]
                else:
                        client_ip = request.META.get('REMOTE_ADDR')
                print(client_ip)
                # client_ip = request.META['REMOTE_ADDR']
                # ingresar la ip en string a la api
                result = lookup.get(client_ip)
                # result = lookup.get('181.51.32.159')
                #obtener latitud y longitud
                latitude = result['latitude']
                longitude = result['longitude']
                # Coordenadas de la ubicación (latitud, longitud)
                coordinates = (latitude, longitude)
                # Crea una instancia de Nominatim
                geolocator = Nominatim(user_agent="pronostico")
                # Obtiene la dirección a partir de las coordenadas
                location = geolocator.reverse(coordinates)
                # informacion del municipio
                InformacionGeneralMunicipio = location.raw
                # informacion del sector de la ubicaci'on
                Municipio = location.raw['display_name'].split(",")
                # nombre del sector
                sector= Municipio[-6]
                # -----
                # crear logica por municipio y sector en Medellin
                # exportar toda la info del municipio por el momento tengo solo un dato
                return HttpResponse("Tu ubicacion es: {}".format(sector))
        
        



        