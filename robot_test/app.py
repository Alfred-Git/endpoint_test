from time import sleep
import requests
import subprocess

host =  'http://172.18.0.2:5000/api'
endpoint = '/check'


while (True):

    response = requests.get(host + endpoint).json()

    # verifico si l respuesta en json es un diccionario y tiene la llave status = "OK"

    if response.get('status') == "ok":
        print('Endpoint is up and running')
	# Envio el registro de conectividad a la rama de prueba 
        subprocess.call('echo "api.endpoint.connection_verified 1 `date +%s`" | nc 172.18.0.4 2003', shell=True)
        
    sleep(60)

    
