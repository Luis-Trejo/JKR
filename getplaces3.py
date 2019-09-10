# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:29:00 2019

@author: Kike
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:31:34 2019

@author: Kike
"""

import json
import csv
import requests
import time
googleGeocodeUrl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?query='
headers={'content-type':'application/json',
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0'}

termino = "restaurantes"
ubicacion = "&location=19.402754,-99.275290&radius=5000"
APIKEY = '&key='+'AIzaSyC2FMyHJmz3ww0VbShyK1j5TzlFlpOufLc'
url = googleGeocodeUrl + termino + ubicacion + APIKEY

def csv_write():
    csvfile=open('restaurantes.csv','w')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["name","lat","long"])
response = requests.get(url=url, headers=headers).json()

     for obj in response['results']:
        writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng']])       
        print ('next_page_token' in response)
        while 'next_page_token' in response:
        URL = url + '&pagetoken=' + response['next_page_token']
        time.sleep(5)
        response = requests.get(url=url, headers=headers).json()
        for obj in response['results']:
            writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng']])
    
else:
        print(response)
if __name__ == '__main__':
    csv_write()
    
    
    



import urllib
import urllib.request
import json

googleGeocodeUrl = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='
termino = "hospitales"
ubicacion = "&location=19.402754,-99.275290&radius=5000"
APIKEY = '&key='+'AIzaSyC2FMyHJmz3ww0VbShyK1j5TzlFlpOufLc'

url = googleGeocodeUrl + termino + ubicacion + APIKEY
print(url)

url = googleGeocodeUrl + termino + ubicacion + APIKEY
json_response = urllib.request.urlopen(url)
busqueda = json_response.read().decode('utf-8')
busquedajson = json.loads(busqueda)

archivolugares = open('ubicacionhospitales.csv','w')
for lugar in busquedajson['results']:
try:
print(lugar['name'])
print(lugar['geometry']['location'])
archivolugares.write(lugar['name']+','+str(lugar['geometry']['location']['lng'])\
 +','+str(lugar['geometry']['location']['lat'])+'\n')
except KeyError as e:
print(e) 
archivolugares.write(lugar['name']+','+str(lugar['geometry']['location']['lng'])\
 +','+str(lugar['geometry']['location']['lat'])+'\n')
archivolugares.close()    