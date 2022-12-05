import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token
import keys
import math
from utils import progress_bar
import random
from customExceptions import SpotifyTokenException

class spotifyClient:    
    def __init__(self,tokenScope):
        self.client_id = keys.client_id
        self.client_secret = keys.client_secret
        # Set up the SpotifyClientCredentials object
        self.client_credentials = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        # Prompt User For Token
        self.token = prompt_for_user_token(scope=tokenScope,
                     client_id=self.client_id, client_secret=self.client_secret, redirect_uri='http://localhost:8888/callback',show_dialog=True)
        # Create Client Object
        if self.token:
            self.client = spotipy.Spotify(auth = self.token)
            self.userData = self.client.me()
            if not self.userData or not self.userData['id']:
                SpotifyTokenException("Can't get user data")
        else:
            SpotifyTokenException("Can't get token")
        
    def createPlayListFromTopTracks(self,top_track_limit,num_of_tracks,playlist_name,playlist_description):
        # Get the user's top tracks
        results = self.client.current_user_top_tracks(limit=top_track_limit)
        top_tracks = [track['id'] for track in results['items']]
        # Calculate how many tracks to get each time 
        num_of_track_per_iteration = math.ceil(num_of_tracks / (top_tracks.__len__() / 5.0))
        # Seed Tracks has limit of 12 so send by batches of 5
        batches = [top_tracks[x:x+5] for x in range(0, len(top_tracks), 5)]
        playlist = []
        #Progress Bar
        progress_bar(0, len(batches))  
        for i, track_list  in enumerate(batches):
            #recommendations(seed_artists=None, seed_genres=None, seed_tracks=None, limit=20, country=None, **kwargs)
            similar = self.client.recommendations(seed_tracks=track_list, limit= num_of_track_per_iteration)  
            for song in similar['tracks']:
                playlist.append(song['uri'])
            progress_bar(i+1,len(batches))  
        #GetRandom songs from list
        random.shuffle(playlist)
        playlist = playlist[:num_of_tracks]
        # Create a new playlist
        created_playlist = self.client.user_playlist_create(self.userData['id'], name=playlist_name, description=playlist_description)
        # Add tracks to the playlist
        self.client.user_playlist_add_tracks(self.userData['id'], created_playlist['id'], playlist)
        # Print the playlist link
        print("\n"+created_playlist['external_urls']['spotify'])


    

