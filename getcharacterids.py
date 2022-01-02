# a script to grab all the character id's and names from the Marvel API for use in my library catologue
import requests
import json


pubKey = '***fillinwithyourmarvelapiinfo***'
privKey = '***fillinwithyourmarvelapiinfo***'
HASH = '***fillinwithyourmarvelapiinfo***'
USER_AGENT = '***fillinwithyourmarvelapiinfo***'

payload = dict()
headers = {'user-agent': USER_AGENT}

# Gateway for API
url = 'http://gateway.marvel.com//v1/public/characters?' # fetches lists of characters

payload['ts'] = 1                # must include as part of auth
payload['apikey'] = pubKey       # must include as part of auth
payload['hash'] = HASH           # must include as part of auth
payload['limit'] = 100


def grabCharIds():
    """ Grabs Character Names and Id #'s from Marvel API"""
    offset = 0
    for apicalls in range(20):
        payload['offset'] = offset
        response = requests.get(url, headers=headers, params=payload)

        count = 0
        for i in response:
            try:

                idfile.write(str(response.json()['data']['results'][count]['name'].ljust(50)))
                idfile.write(str(response.json()['data']['results'][count]['id']))
                idfile.write("\n")
                count += 1
            except IndexError:
                print('No more comics')
                break

        offset += 100

if __name__ == "__main__":

    idfile = open("marv_char_ids.txt", "w")
    grabCharIds()
    idfile.close()
