#Making a Raw HTTP Connection to Google Map

# -*- codin: UTF-8 -*-

import http.client
import json
from urllib.parse import quote_plus


base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base,quote_plus(address))
    print(path)
    user_agent = b'Python Network'
    print(user_agent)
    headers = {b'User-Agent':user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    print(connection)
    connection.request('Get',path,None,headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    #print(reply)
    #print(reply[0]['lat'],reply[0]['lon'])


    #base = 'https://nominatim.openstreetmap.org/search'
    #parameters = {'q': address,'format':'json'}
    #user_agent = 'Python Network'
    #headers = {'User-Agent': user_agent}
    #response = requests.get(base,params=parameters,headers=headers)
    #reply = response.json()



if __name__ == '__main__':
    geocode('207 N. Defiance St,Archbold, OH')



