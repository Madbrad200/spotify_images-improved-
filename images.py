################################################################################
# Original Author: Orion Crocker
# Fork Author: Madbrad200
# Filename: images.py
# Date: 02/06/20
# 
# Get Spotify Album Art
# Retrieves album art from Spotify's spotify
################################################################################

import api
import os
import requests
from zipfile import ZipFile
from datetime import datetime


def rename(name):
    # remove any illegal characters and strip empty spaces
    return name.replace("/", "").replace("<", "").replace(">", "").replace(":", "").replace("\"", "").replace("\\", "").replace("|", "").replace("?", "").replace("*", "").strip()


def zip_images(directory):
    zip_this = ZipFile(directory + '.zip', 'w')
    os.chdir(directory)
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            zip_this.write(file)
    zip_this.close()


def url_to_uri(uri, typeof):
    offset = uri.find(typeof)
    return 'spotify:' + uri[offset:].replace('/', ':')


def get_images(url, directory=None, verbose=False, zip_this=False):
    typeof = ''
    results = ''
    if 'artist' in url:
        typeof = 'artist'
        results = api.get_artist(url)
    elif 'playlist' in url:
        typeof = 'playlist'
        results = api.get_playlist(url)
    if results == '':
        print("No results found, check URL and try again.")
        exit(1)
    else:
        print(typeof + " found, downloading...")

    if typeof == 'artist':
        name = results['items'][0]['artists'][0]['name']
        results = results['items']

    count = 0 
    pics = []
    
    today = datetime.now()
    # create folder with current date/time as folder name
    if directory:
        directory = directory + '/' + rename(today.strftime('%Y-%m-%d-%H-%M-%S'))
    else:
        directory = 'results/' + rename(today.strftime('%Y-%m-%d-%H-%M-%S'))

    if not os.path.exists(directory):
        os.makedirs(directory)

    for track in results:
        if typeof == 'artist':
            url = track['images'][0]['url']
            name = rename(track['name'])
        elif typeof == 'playlist':
            url = track['track']['album']['images'][0]['url']  # grab image url
            artist_name = rename(track['track']['artists'][0]['name'])  # grab artist name
            album_name = rename(track['track']['album']['name'])  # grab album name
            name = f"{artist_name} - {album_name}"  # this will become the name of the file
     
        path = directory + '/' + name + '.jpeg'
        if os.path.exists(path):
            continue

        pic = requests.get(url, allow_redirects=True)

        if verbose:
            print(path)

        try:
            open(path, 'wb').write(pic.content)
            count += 1
            pics.append(pic)
        except OSError as e:
            print(f"{e}\nSkipping..")

    print(str(len(pics)) + " saved to " + directory)

    if zip_this:
        zip_images(directory)

    return directory
