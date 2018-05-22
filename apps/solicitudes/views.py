from django.shortcuts import render
import requests, json, os
from django.http import HttpResponse
import base64
# Create your views here.

def solicitud(id=None):
	#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	#files = {
	#	'file': (open(BASE_DIR+'/solicitudes/image.jpg', 'rb'), 'image/jpg', {'Expires': '0'})
	#}

	headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
       
    }
	url = 'http://mundogolf.com.do/api/v1/crear-producto.php'
	#image_file = open(BASE_DIR+'/solicitudes/image.jpg', 'rb')	
	#image_read = image_file.read()
	#img = base64.encodestring(image_read)
	#print(img)
	datos = {
            "ProductoEspecificacion": [{
                "nombre": "MARCA",
                "valor": "HJ"
            }, {
                "nombre": "SEXO",
             			"valor": "UNISEX"
            }, {
                "nombre": "COLOR",
             			"valor": "BLACK"
            }, {
                "nombre": "TAMAÑO",
             			"valor": "LARGE"
            }, {
                "nombre": "MODELO",
             			"valor": "SOL SLEEVE"
            }
            ],
            "ProductoImagen": [],
            "stock": 8,
            "padre": 0,
            "accion": 0,
            "codigo": "",
            "codigo_interno": "00200376",
            "codigo_interno_padre": "00200190",
            "categoria": "SLEEVES",
            "impuesto": 18,
            "codigo_barra": "00200376",
            "nombre": "HJ SLEEVES SOL SLEEVE UNISEX BLACK LARGE",
            "nombre_es": "HJ SLEEVES SOL SLEEVE UNISEX BLACK LARGE",
            "nombre_en": "HJ SLEEVES SOL SLEEVE UNISEX BLACK LARGE",
            "descripcion_corta_es": "El par de mangas \u003ci\u003eSol Sleeve\u003c/i\u003e protegen contra la exposición excesiva al sol que daña la piel. Con una calificación UPF de 50+, estas mangas bloquean el 98% de los rayos UV-A / UV-B. Probado de acuerdo con los estándares AATCC 183. Sin mencionar que este gran producto también elimina la humedad y es perfecto para múltiples actividades en exteriores. ¡La tabla de tallas para damas y hombres por igual!",
            "descripcion_corta_en": "The \u003ci\u003eSol Sleeve\u003c/i\u003e pair protect yourself from over exposure of skin damaging sun. UPF rating of 50+, these Sol Sleeves block 98% of UV-A/UV-B rays. Tested according to AATCC 183 standards. Not to mention this great product also wicks away moisture and is perfect for multi-outdoor activities. The Sizing chart for ladies and men alike!",
            "descripcion_es": "\u003cb\u003eHJ Sol Sleeves\u003c/b\u003e\r\n\u003cbr\u003e\u003c/br\u003e\r\nEl par de mangas \u003ci\u003eSol Sleeve\u003c/i\u003e protegen contra la exposición excesiva al sol que daña la piel. Con una calificación UPF de 50+, estas mangas bloquean el 98% de los rayos UV-A / UV-B. Probado de acuerdo con los estándares AATCC 183. Sin mencionar que este gran producto también elimina la humedad y es perfecto para múltiples actividades en exteriores. ¡La tabla de tallas para damas y hombres por igual!\r\n",
            "descripcion_en": "\u003cb\u003eHJ Sol Sleeves\u003c/b\u003e\r\n\u003cbr\u003e\u003c/br\u003e\r\nThe \u003ci\u003eSol Sleeve\u003c/i\u003e pair protect yourself from over exposure of skin damaging sun. UPF rating of 50+, these Sol Sleeves block 98% of UV-A/UV-B rays. Tested according to AATCC 183 standards. Not to mention this great product also wicks away moisture and is perfect for multi-outdoor activities. The Sizing chart for ladies and men alike!\r\n",
            "precio": 24.9924,
            "precio_sin_itbis": 21.18,
            "precio_regular": 24.9924,
            "disponible": 1,
            "en_especial": 0,
            "novedad": 0,
            "cant_tiempo_entrega": 30,
            "tiempo_entrega": "HORA",
            "orden": 660339,
            "inicio_venta": "\/Date(1478750400000)\/",
            "fin_venta": "\/Date(-62135582400000)\/",
            "estado": 3
        }

	response = requests.post(url, data=json.dumps(datos), headers=headers)

	return HttpResponse(response)
