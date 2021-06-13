import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getConfig():
    #get config file
    #return lines as arr
    f = open("config.txt", "r")
    fstr = f.read()
    farr = fstr.split(",")
    return farr


def main():
    configArr = getConfig()
    
    CLIENT_ID = configArr[0]
    CLIENT_SECRET = configArr[1]


    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    print(access_token)

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    r = requests.get(BASE_URL + "search?q=Brittany%20Howard&type=artist&market=GB&limit=1", headers=headers)


    d = r.json()

    id = d['artists']['items'][0]['id']
    #print(d['artists']['items'][0]['id'])

    r = requests.get(BASE_URL + "artists/" + id + "/albums?market=GB", headers=headers)
    d = r.json()
    #print(json.dumps(d['items'][0], indent=4, sort_keys=True))
    #print(d['items'][0]['id'])

    id = d['items'][0]['id']
    r = requests.put(BASE_URL + "me/albums?ids=" + id, headers=headers)
    d = r.json()
    print(d)

if __name__ == '__main__':
    main()