#Fetching a JSON Document from the nominatim

# -*- codin: UTF-8 -*-

import requests 

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address,'format':'json'}
    user_agent = 'Python Network'
    headers = {'User-Agent': user_agent}
    #get a webpage
    response = requests.get(base,params=parameters,headers=headers)
    reply = response.json()
    #print(reply)

    print('lat:'+reply[0]['lat'],'lon:'+reply[0]['lon'])


if __name__ == '__main__':
    geocode('207 N. Defiance St,Archbold, OH')



