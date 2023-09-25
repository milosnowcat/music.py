import spotipy
import spotipy.util as util
import pyautogui

def fetchPlaylist(client_id, client_secret, redirect_uri, username, playlist_id):
    scope = "playlist-read-private"

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    sp = spotipy.Spotify(auth=token)
    playlist = sp.playlist(playlist_id)

    tracks = playlist["tracks"]["items"]

    songs = set()

    for track in tracks:
        song_name = track["track"]["name"]
        song_artist = track["track"]["artists"][0]["name"]
        songs.add(song_name + " - " + song_artist)

    return songs

def write(text):
    pyautogui.write(text)
    pyautogui.press("enter")
