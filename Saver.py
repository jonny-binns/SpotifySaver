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

def getAlbumList(path):
    musicList = []
    artistList = os.listdir(path)
    for a in artistList:
        albumList = os.listdir(path + "/" + a)
        for al in albumList:
            musicList.append(a + ":" + al)
    return musicList

def getPath():
    path = input("Enter the relative path to your music folder, be sure not to have a / as the final character: ")
    return path


def main():

    path = getPath()
    albumList = getAlbumList(path)

    configArr = getConfig()
    os.environ["SPOTIPY_CLIENT_ID"] = configArr[0]
    os.environ["SPOTIPY_CLIENT_SECRET"] = configArr[1]
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8000"

    scope = "user-library-modify"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    notSaved = []

    for a in albumList:
        albumArr = a.split(":")
        
        result = sp.search(albumArr[0], limit=50, offset=0, type='album', market='GB')

        saved = []
        notFound = True
        for i in result['albums']['items']:
     
            if a not in saved:
                if i['name'] == albumArr[1]: 
                    #print(json.dumps([i], indent=4, sort_keys=True))
                    result = sp.current_user_saved_albums_add([i['id']])
                    if result == None:
                        saved.append(a)
                        #print(result)
                        print("Saved: " + albumArr[0] + " - " + albumArr[1])
                        notFound = False

        if notFound == True:
            print("FAILED: " + albumArr[0] + " - " + albumArr[1])
            notSaved.append(a)
    

    f = open("error.txt", "w")
    f.close()
    notSaved = list(dict.fromkeys(notSaved))
    
    for a in notSaved:
        f = open("error.txt", "a")
        f.write(str(a) + "\n")
        f.close()


if __name__ == '__main__':
    main()


    '''
    result = sp.search('Aphex Twin', limit=50, offset=0, type='album', market='GB')
    #print(json.dumps(result, indent=4, sort_keys=True))
    for i in result['albums']['items']:
        print(i['name'])
    '''

            # print(json.dumps(result, indent=4, sort_keys=True))
        #print(dir(result))
        #print(result['albums']['items'][0]['id'])

        #id = result['albums']['items'][0]['id']