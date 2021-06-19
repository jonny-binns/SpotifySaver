import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
import json

def getConfig():
    #get config file
    #return lines as arr
    f = open("config.txt", "r")
    fstr = f.read()
    farr = fstr.split(",")
    return farr

def getAlbumList():
    musicList = []
    artistList = os.listdir("Music")
    for a in artistList:
        albumList = os.listdir("Music/" + a)
        for al in albumList:
            musicList.append(a + ":" + al)
    return musicList


def main():
    albumList = getAlbumList()

    configArr = getConfig()
    os.environ["SPOTIPY_CLIENT_ID"] = configArr[0]
    os.environ["SPOTIPY_CLIENT_SECRET"] = configArr[1]
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"

    scope = "user-library-modify"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    for a in albumList:
        albumArr = a.split(":")
        
        result = sp.search(albumArr[0], offset=0, type='album', market='GB')
        #print(json.dumps(result, indent=4, sort_keys=True))
        #print(dir(result))
        #print(result['albums']['items'][0]['id'])

        #id = result['albums']['items'][0]['id']
        for i in result['albums']['items']:
            if i['name'] == albumArr[1]:
                result = sp.current_user_saved_albums_add([i['id']])
                print(result)

if __name__ == '__main__':
    main()