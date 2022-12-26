
Documentar todo con https://www.django-rest-framework.org/coreapi/from-documenting-your-api/
# GeolocalizacionDjango

![GitHub repo size](https://img.shields.io/github/repo-size/diegomolinaquintero/GeolocalizacionDjango)
![GitHub](https://img.shields.io/github/license/diegomolinaquintero/GeolocalizacionDjango?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/diegomolinaquintero/GeolocalizacionDjango)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/diegomolinaquintero/GeolocalizacionDjango)

Este proyecto tiene como objetivo dar el nombre del barrio, corregimiento o sector del Área metropolitana y Valle de Aburra de Antioquia, Colombia.

# Comó funciona?

Solo debes hacer que el usuario ingrese a la direcci'on  de tu app, con esto obtenemos la ip, esto lo transformamos en latitud y longitud con [https://surfy.one/geoip](https://surfy.one/geoip "https://surfy.one/geoip") 

# Dos metodos para obtener los datos
Como este proyecto esta prueba, tenemos dos formas de dar la informaci'on

### Metodo 1
Usamos la API de [Surfy](https://surfy.one/geoip "Surfy") obtenemos el json y filtramos solo por la ciudad

### Metodo 2
Usamos la API de [Surfy](https://surfy.one/geoip "Surfy") para obtener solo longitud y latitud, estos datos son pasado por [geopy.geocoders](https://geopy.readthedocs.io/en/stable/ "geopy.geocoders") el cual nos entrega una gran cantidad de informaci'on, nosotros la filtramos y obenemos el sector o municipo donde se encuentra el usuario.

