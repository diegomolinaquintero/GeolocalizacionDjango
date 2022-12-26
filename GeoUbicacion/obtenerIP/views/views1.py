from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# una api free con contribuciones de este year
from geoip import GeoIP
# probar esta que esta pensada para pytohn
# import geoip2_extras
import json
import os
#traer email y key para no quemarlos en el codigo
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


class EncontrarUbicacion1(APIView):
        def get(self, request):
                #api key gratis de https://surfy.one/geoip
                lookup = GeoIP(get_secret('emailApiSurfy'), get_secret('keyApiSurfy'))
                #ip usaurio https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.META
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
                print(result)
                # -----
                # crear logica por municipio y sector en Medellin
                
                
                        # Do something with the client IP address
                return HttpResponse("Estas ubicado cerca a: {}".format(result['city']))



