import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import os
import siriusxm


def add_to_queue(sp: spotipy.Spotify, channel: str):
    ch = siriusxm.get_channel(channel)

    for song in ch:
        if 'spotify' in song.keys():
            print(f"Adding: {song['track']['name']} by: {song['track']['artists']}")
            sp.add_to_queue(song['spotify']['spotify_id'])
        else:
            print(f"No spotify data for: {song['track']['name']} by: {song['track']['artists']}")


def refresh():
    token_info = sp_oauth.get_cached_token()

    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(auth_url)
        response = input('Paste the above link into your browser, then paste the redirect url here: ')

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)

    token = token_info['access_token']

    sp = spotipy.Spotify(auth=token)

    return sp


if __name__ == '__main__':
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    scope = [
        'app-remote-control',
        'playlist-modify-public',
        'user-read-playback-state',
        'user-modify-playback-state',
        'user-read-currently-playing'
    ]

    redirect_uri = 'https://localhost'


    sp_oauth = oauth2.SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope)
    
    sp = refresh()