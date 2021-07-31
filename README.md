# SpotifySaver
Basic program to go through your folders of music and save them to your spotify

This program will only work for music folders structured in the format "~/Artist/Album", this program does not read the tags of the music so folder names need to be accurate

# KNOWN ISSUES
    Because this program is so simple there are some problems with it that may not be fixed
* Explicit content, since spotify does include whether an album has explicit songs this program takes the first instance of the album that is returned and saves that. This means there is no control as to whether an explicit version of an album is saved
* Album names, if the name of the album folder is not the same as the name of the album on spotify it may not be saved, these albums will be included in the error.txt file


# Instructions
1. Make a spotify developer account and create an application (I named mine AlbumSaver)
2. Go to edit settings and add "http://localhost:8000" as the redirect URL (on first run you will be sent there to enter your spotify credentials)
3. Clone this repo
4. In the folder this repo is saved in create a file called config.txt
5. Go back to the spotify application dashboard, here copy your ClientID and Client Secret to config.txt in the format "(ClientID),(Client Secret)"
6. Run the application like you would any other python app and sign in when prompted

# Dependencies
* Spotipy

### To-Do List
* Add error handling to getConfig()
* Create config.txt if it doesn't exist
