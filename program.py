import spotify
from utils import getNumericalValue,getStringValue
from customExceptions import SpotifyTokenException

def getClient():
    while True:
        try:
            spotifyClient = spotify.spotifyClient("user-top-read playlist-modify-public")
            return spotifyClient
        except SpotifyTokenException as e:
            print(e)
            
spotifyClient = getClient()
# Ask the user to enter the number of tracks to add to the playlist
num_tracks = getNumericalValue(message= "Please enter the number of tracks to add to the playlist.(Only numbers from 1-100 are allowed): ", min=1,max=100)
# Ask the user to enter the playlist name and description
playlist_name = getStringValue(message= "Please enter a name for the playlist:(Must be non-empty and must be maximum 100 character) ", min=1,max=100)
playlist_description = getStringValue(message= "Please enter a description for the playlist:(Must be maximum 300 character) ", min=0,max=300)

#Create Playlist
spotifyClient.createPlayListFromTopTracks(top_track_limit = 100, num_of_tracks = num_tracks,playlist_name = playlist_name,playlist_description = playlist_description)


