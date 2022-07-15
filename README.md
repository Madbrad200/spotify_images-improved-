# spotify\_images
`spotify_images` provides a simple method of retrieving all unique album art from either a Spotify playlist and creating a collage from the query.

This fork will allow you to grab all images from a playlist, regardless of size, along with neater file names!

The original script would stop short once it hit the 100th track in a playlist. This *is no longer the case* - large playlists will have their single/album arts downloaded in their entirety.

I've added some comments where I feel an explanation would help readability, and complied with flake8 guidelines.

## Installation:

If you're on windows, I'd recommend setting up a virtual environment first:

```bash
python3 -m venv /path/to/new/virtual/environment
```

Entering your venv [depends on how you are accessing the terminal](https://docs.python.org/3/library/venv.html), in Powershell, simply type:
```bash
/path/to/new/virtual/environment/Scripts/Activate
```

Then, or if you skipped the venv process entirely, you can clone the github:

```bash
git clone https://github.com/Madbrad200/spotify_images-improved-
```

Done!

## Setup:
Before using this program, you'll need to get credentials from [Spotify's API](https://developer.spotify.com/documentation/web-api/quick-start/).
An account on Spotify will provide two credentials: 'client id' and 'client secret.'

Modify the `config.py` file's two fields:
```python
client_id = 'your_client_id'
client_secret = 'your_client_secret'
```

**Never publish your ID publicly**

Two prerequisites you'll need installed on your machine are [pillow](https://pillow.readthedocs.io/en/stable/installation.html) and [spotipy](https://spotipy.readthedocs.io/en/master/).
You can easily get both of these from the `pip` repository.
If you aren't yet aware of the beauty of `pip`, go check out [it's website](https://pypi.org/project/pip/).
You're welcome.

```bash
pip3 install -r requirements.txt
```

Or install manually:
```bash
python3 -m pip install pillow
python3 -m pip install spotipy
```

# Usage:

## Download album art from an artist or playlist:
By default `spotify_images` fetches all unique art of any Spotify arist or playlist link given as an argument
```bash
python3 main.py https://open.spotify.com/playlist/13OSe3KLY2qnUrdP2Sv6j7
```

## Verbose
Use the `-v` or `--verbose` flag to see what the program is doing in real time.

## Create a collage
Use the `-c` or `--collage` collage flag to create a collage of the artwork downloaded.

Example collage:

![Unleash The Archers Collage](examples/collage.jpeg)
