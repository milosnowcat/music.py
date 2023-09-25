import spotipy
import spotipy.util as util
import pyautogui

def fetchPlaylist(client_id, client_secret, redirect_uri, username, playlist_id):
    """
    The function fetchPlaylist retrieves the songs from a specified playlist using the Spotify API.
    
    :param client_id: The client_id is a unique identifier for your application. You can obtain it by
    creating a Spotify Developer account and registering your application
    :param client_secret: The `client_secret` parameter is a confidential string that is used to
    authenticate the client application with the Spotify API. It is typically provided by Spotify when
    you register your application with their developer platform
    :param redirect_uri: The redirect_uri is the URI where the user will be redirected after granting
    permission to access their Spotify account. It is typically a URL of your application or website
    :param username: The username is the Spotify username of the user whose playlist you want to fetch
    :param playlist_id: The `playlist_id` parameter is the unique identifier for the playlist you want
    to fetch. It is a string that looks something like "37i9dQZF1DXcBWIGoYBM5M" for a Spotify playlist
    :return: The function fetchPlaylist returns a set of songs in the format "song name - artist name".
    """
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
    """
    The function "write" uses the pyautogui library to type the given text and press the enter key.
    
    :param text: The parameter "text" is a string that represents the text you want to write
    """
    pyautogui.write(text)
    pyautogui.press("enter")
