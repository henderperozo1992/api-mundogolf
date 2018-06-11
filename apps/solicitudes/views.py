from django.shortcuts import render
import requests, json, os
from django.http import HttpResponse
import base64
import codecs
# Create your views here.
import logging

def solicitud(id=None):
	LOG_FILENAME = 'LogCreateUser.log'
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	listFiles = os.listdir("../../productos_padres")
	
	with open('../../productos_padres/Padre-00900962.json', encoding='utf-8-sig') as fileOpen:

		data = json.load(fileOpen)
		headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
		
		}
	url = 'https://mundogolf.net/api/v1/crear-producto.php'

	datos=data
	response = requests.post(url, data=json.dumps(datos), headers=headers)
	logging.debug(response)
	return HttpResponse(response)
