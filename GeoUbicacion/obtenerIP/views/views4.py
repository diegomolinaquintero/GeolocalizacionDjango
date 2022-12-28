import googlemaps
from django.http import HttpResponse
from rest_framework.views import APIView
#traer email y key para no quemarlos en el codigo
import json
import os
from GeoUbicacion.settings import BASE_DIR
from django.core.exceptions import ImproperlyConfigured
import requests

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
        secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
        """Get secret setting or fail with ImproperlyConfigured"""
        try:
                return secrets[setting]
        except KeyError:
                raise ImproperlyConfigured("Set the {} setting".format(setting))

class EncontrarUbicacion4(APIView):
        """Encuentra tu sector o barrio del valle de aburra y area
        metropolitada desde donde te conectas.

        Esta es una forma de realizar la busqueda.

        Notes
        -----
        Usando la api de google ubicamos el usuarios, te da el barrio , ciudad y el pronostico que ofrece el SIATA.

        Puedes tener muchos datos importantes pero para este codigo
        solo mostramos el sector y/o barrio.

        Puedes modificar la funcion para mostrar mas datos.
        """
        def get(self, request):
                gmaps = googlemaps.Client(key=get_secret('googleApiKeyPersonal'))
                # Look up an address with reverse geocoding
                geolocate = gmaps.geolocate()
                latitude = geolocate['location']['lat']
                longitude = geolocate['location']['lng']
                geodirection = gmaps.reverse_geocode((latitude, longitude))
                # geodirection = gmaps.reverse_geocode((6.284241285323519, -75.58133158794963))
                address = geodirection[0]['formatted_address']
                Municipio = geodirection[0]['formatted_address'].split(",")
                MunicipioSinEspacios = [elemento.strip() for elemento in Municipio]
                medellinCentro = ['La America', 'Ferrini', 'Calasanz','Los Pinos','La Floresta','Santa Lucia','El Danubio','Campo Alegre','Santa Monica','Barrio Cristóbal','Simon Bolivar','Santa Teresita','Calasanz Parte Alta','Los Conquistadores','Laureles','Carlos E. Restrepo','Suramericana','Naranjal','San Joaquin','Bolivariana','Las Acacias','La Castellana','Lorena','El Velodromo','Estadio','Los Colores','Cuarta Brigada','Florida Nueva','Villa Hermosa','La Mansion','San Miguel','La Ladera','Golondrinas','Batallon Girardot','Llanaditas','Los Mangos','Enciso','Sucre','El Pinal','13 de Noviembre','La Libertad','Villatina','San Antonio','Las Estancias','Villa Turbay','La Sierra','Villa Lilliam','Esfuerzos de Paz I','Esfuerzos de Paz II','Buenos Aires','Caicedo','Juan Pablo II','Ocho de Marzo','Barrios de Jesus','Bombona II','Los Cerros','El Vergel','Alejandro Echavarría','Miraflores','Cataluña','La Milagrosa','Gerona','El Salvador','Loreto','Asomadera I','Asomadera II','Asomadera III','Quinta Linda','Barrio Pablo Escobar','La Candelaria','Prado','Jesus Nazareno','El Chagualo','Estacion Villa','San Benito','Guayaquil','Corazon de Jesus','Barrio Triste','Calle Nueva','Perpetuo Socorro','Barrio Colon','Las Palmas','Bombona I','Boston','Los Angeles','Villa Nueva','San Diego']
                medellinOriente = ['Popular','Popular I','Popular II','Santo Domingo','Santo Domingo Savio I','Santo Domingo Savio II','Granizal','Moscu II','Villa Guadalupe','San Pablo','Aldea Pablo VI','La Esperanza II','El Compromiso','La Avanzada','Carpinelo','Santa Cruz','La Isla','El Playon de Los Comuneros','Pablo VI','La Frontera','La Francia','Andalucia','Villa del Socorro','Villa Niza','Moscu I','La Rosa','Castropol','Barrio Colombia','Villa Carlota','Lalinde','Manila','Las Lomas I','Las Lomas II','Altos del Poblado','Poblado','El Tesoro','Los Naranjos','Los Balsos I','Los Balsos II','San Lucas','El Diamante','El Castillo','Alejandria','La Florida','El Poblado','Astorga','Patio Bonito','La Aguacatala','Santa Maria de Los Angeles', 'El Poblado','La Salle','Las Granja','Campo Valdes','Campo Valdes II','Santa Ines','El Raizal','El Pomar','Manrique Central II','Manrique Oriental','Versalles I','Versalles II', 'Versalles','La Cruz','La Honda','Oriente','Maria Cano','Carambolas','Maria Cano – Carambolas','San Jose La Cima I' ,'San Jose La Cima II','Manrique','Aranjuez','Berlin','San Isidro','Palermo','Bermejal','Los Alamos','Bermejal – Los Álamos','Moravia','Sevilla','San Pedro','Manrique Central I','Campo Valdes I','Las Esmeraldas','La Piñuela','Brasilia','Miranda']
                medellinOccidente = ['Castilla','Toscana','Héctor Abad Gómez','La Paralela','Las Brisas','Florencia','Tejelo','Boyacá','Belalcazar','Girardot','Tricentenario','Francisco Antonio Zea','Alfonso López','Caribe','El Progreso','12 de Octubre','12 de Octubre I','12 de Octubre II','Doce de Octubre I','Doce de Octubre I','Santander','Pedregal','La Esperanza','San Martín de Porres','Kennedy','Picacho','Picachito','Mirador del Doce','El Progreso','El Progreso II','El Triunfo','Robledo','El Volador','San Germán','Barrio Facultad de Minas','La Pilarica','Bosques de San Pablo','Altamira','Córdoba','López de Mesa','El Diamante','Aures','Aures I','Aures II','Bello Horizonte','Villa Flora','Palenque','Cucaracho','Fuente Clara','Santa Margarita','Olaya Herrera','Pajarito','Monteclaro','Villa de La Iguaná','La Cuchilla','La Aurora','Aurora','Tenche','Trinidad','Santa Fe','Campo Amor','Cristo Rey','Guayabal','La Colina','Belén','Belen','Cerro' 'Nutibara','Fátima','Fatima','Rosales','Granada','San Bernardo','Las Playas','Diego Echavarria','La Mota','El Rincón','El Rincon','La Hondonada','La Loma de Los Bernal','La Gloria','Altavista','La Palma','Zafra','Los Alpes','Las Violetas','Las Mercedes','Nueva Villa de Aburrá','Villa de Aburrá','Villa de Aburra','Miravalle','El Nogal – Los Almendros','El Nogal','Los Almendros']
                Palmitas = ['Palmitas']
                Caldas  = ['Caldas']
                Copacabana = ['Copacabana']
                Estrella = ['La Estrella']
                Itagui = ['Itagüi']
                Bello = ['Bello']
                Envigado = ['Envigado']
                Sabaneta = ['Sabaneta']
                Barbosa = ['Barbosa']
                Girardota = ['Girardota']
                pronostico = 'default'
                #Palmitas
                if any(element in MunicipioSinEspacios for element in set(Palmitas)):
                    pronostico = 'el de Palmitas'
                #Caldas
                if any(element in MunicipioSinEspacios for element in set(Caldas)):
                    pronostico = 'el de caldas'
                #Copacabana    
                if any(element in MunicipioSinEspacios for element in set(Copacabana)):
                    pronostico = 'Copacabana'
                #Estrella
                if any(element in MunicipioSinEspacios for element in set(Estrella)):
                    pronostico = 'el de Estrella'
                #Itagui    
                if any(element in MunicipioSinEspacios for element in set(Itagui)):
                    pronostico = 'Itagui' 
                #Bello
                if any(element in MunicipioSinEspacios for element in set(Bello)):
                    pronostico = 'el de Bello'
                #Envigado    
                if any(element in MunicipioSinEspacios for element in set(Envigado)):
                    pronostico = 'Envigado'
                #Sabaneta
                if any(element in MunicipioSinEspacios for element in set(Sabaneta)):
                    pronostico = 'el de Sabaneta'
                #Barbosa    
                if any(element in MunicipioSinEspacios for element in set(Barbosa)):
                    pronostico = 'Barbosa'
                #Girardota    
                if any(element in MunicipioSinEspacios for element in set(Girardota)):
                    pronostico = 'Girardota' 
                #medellinOccidente   
                if any(element in MunicipioSinEspacios for element in set(medellinOccidente)):
                    pronostico = 'medellinOccidente'
                #medellinOriente    
                if any(element in MunicipioSinEspacios for element in set(medellinOriente)):
                    pronostico = 'medellinOriente'
                #medellinCentro    
                if any(element in MunicipioSinEspacios for element in set(medellinCentro)):
                    pronostico = 'medellinCentro'
                
                return HttpResponse("Estas cerca de : {} y su pronostico es {}".format(address,pronostico))
        
        



        