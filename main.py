from config import client_id, secret_id
from tracklist import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import argparse
import logging

# logger = logging.getLogger('examples.create_playlist')
# logging.basicConfig(level='DEBUG')

def create_playlist(sp, user_id, title, description, tracks):
    playlist = sp.user_playlist_create(user=user_id, name=title, description=description)
    results = sp.user_playlist_add_tracks(user_id, playlist["id"], tracks)
    return results['snapshot_id']

def main():
    
    scope = "user-read-private playlist-modify-public playlist-modify-private" 
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                        client_id=client_id, client_secret=secret_id, 
                        redirect_uri="http://localhost:8080"))
    
    username = sp.me()['id']

    url = input("Please enter the 1001tracklists.com URL to create the Spotify playlist: ")
    tracklist = Tracklist(url)
    tracks = tracklist.get_track_list()
    title = tracklist.get_title()
    spot_ids = tracklist.get_clean_spotify_links()


    print(f'\nYou are about to create a new Spotify playlist, {title}, with {len(tracks)} tracks on account: {username}.\n')
    for i, t in enumerate(tracks):
        print(i, t)
    if input("\nAre you sure? (y/n)") != "y":
        exit()
    res = create_playlist(sp, username, title, url, spot_ids)
    print(f'\nPlaylist successfully created! (snapshot_id: {res})')

if __name__ == '__main__':
    main()
