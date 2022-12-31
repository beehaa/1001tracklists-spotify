from config import client_id, secret_id
from tracklist import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth


import argparse
import logging

logger = logging.getLogger('examples.create_playlist')
logging.basicConfig(level='DEBUG')

def get_args():
    parser = argparse.ArgumentParser(description='Create a playlist for user from tracklists URL')
    parser.add_argument('-u', '--url', required=True, help='Tracklist URL')
    return parser.parse_args()

def create_playlist(sp, user_id, title, description):
    playlist = sp.user_playlist_create(user=user_id, name=title, description=description)
    return playlist["id"]

def add_tracks_to_playlist(sp, user_id, playlist_id, tracks):
    sp.user_playlist_add_tracks(sp, user_id, playlist_id, tracks)
    return

def main():
    # args = get_args()
    # print(args.url)
    url = r'https://www.1001tracklists.com/tracklist/m0gsy41/tiesto-club-life-820-aftrhrs-yearmix-2022-12-16.html'
    tl = Tracklist(url)
    print(tl.title)
    print(tl.tracklist_id)
    print(tl.tracks)
    # tracks = tl.spotify_links
    # title = tl.title
    # desc = f"{tl.title} - {tl.artist}"

    
    # scope = "user-read-private playlist-modify-public" 
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
    #                 client_id=client_id, client_secret=secret_id, 
    #                 redirect_uri="http://localhost:8080"))
    # user_id = sp.me()['id']
    

if __name__ == '__main__':
    main()