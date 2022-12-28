import googlemaps
from django.http import HttpResponse
from rest_framework.views import APIView
#traer email y key para no quemarlos en el codigo
import json
import os
from geopy.geocoders import Nominatim
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

class EncontrarUbicacion3(APIView):
        """Encuentra tu sector o barrio del valle de aburra y area
        metropolitada desde donde te conectas.

        Esta es una forma de realizar la busqueda.

        Notes
        -----
        Mostrar la tu direccion, barrio, ciudad y departamento con la api de google.
        """
        def get(self, request):
                gmaps = googlemaps.Client(key='AIzaSyCWvPEoQjPCqKCcgHfUSoaMmdFa48Y_8B8')
                # Look up an address with reverse geocoding
                geolocate = gmaps.geolocate()
                latitude = geolocate['location']['lat']
                longitude = geolocate['location']['lng']
                geodirection = gmaps.reverse_geocode((latitude, longitude))
                address = geodirection[0]['formatted_address']
                return HttpResponse("Estas cerca de : {}".format(address))
        
        



        