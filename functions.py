# Quick Play Imports
import deezer
import keyboard
import time
import random

client = deezer.Client()
###TEXT FUNCTIONS :##########################################################

def get_available_user_from_txt(plateform) :
    if plateform == "Deezer" :
        user_list = []
        with open("user_deezer.txt", "r") as f :
            for x in f :
                user_list.append((x[:10],x[11:].replace("\n","")))
        return(user_list)
    elif plateform == "Spotify" :
        user_list = []
        with open("user_spotify.txt", "r") as f :
            for x in f :
                l = x.split(" ")
                user_list.append((l[0],l[1].replace("\n","")))
        return(user_list)
    else :
        raise NameError("Invalid plateform")

def get_artist(track):
    string = (track.get_artist()).__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

def get_title(track):
    string = track.__repr__()
    string = string[1:-1]
    string = string.split(" ",1)
    return(string[1])

def get_str_from_list(liste) :
    for i,track in enumerate(liste) :
        title  = get_title(track)
        author = get_artist(track)
        liste[i] = title + " " + author

    return(liste)

def paste_list(liste,p="!p",t=1):
    time.sleep(5)
    for x in liste :
        x = p +" "+ x
        keyboard.write(x)
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        time.sleep(t)

def get_playlists_name_list(liste) :
    new_list = []
    for i,elem in enumerate(liste) :
        string = (((elem.__repr__())[1:-1]).split(" ",1))[1]
        new_list.append(string)
    return new_list

def print_track_list(track_list,randomise,limitation,plateform,t,prefix="/play") :
    if randomise == True :
        random.shuffle(track_list)
    if 1 <= limitation <= len(track_list) :
        track_list = track_list[:limitation]

    if plateform == "Deezer" :
        paste_list(get_str_from_list(track_list),t=t,p=prefix)
    elif plateform == "Spotify" :
        paste_list(track_list,t=t,p=prefix)
    else :
        raise NameError('Invalid plateform')

###DEEZER FUNCTIONS :##########################################################

def get_user(username) :
    return client.get_user(username)

def get_playlists(username) :
    user = get_user(username)
    return user.get_playlists()

def get_tracks(playlist):
    return playlist.get_tracks(limit='1000')
