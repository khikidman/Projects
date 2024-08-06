import requests
import json
import sys

CLIENT_ID = 'ffce952d017245b191dcf95415691f40'
CLIENT_SECRET = '01809d81cb9247b1848d2d6cbbf471cf'
USER_ID = 'khi.kidman'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response =  requests.post(AUTH_URL,  {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data["access_token"]

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

playlist_id = '0fnYNg9zNoLEfJVU9f43GB'

# r = requests.get(BASE_URL + 'users/' + USER_ID + '/playlists', headers=headers)

# playlists = r.json()

# print(playlists)

# with open('./playlists.json', 'w', encoding='utf-8') as f:
#     json.dump(playlists, f, ensure_ascii=False, indent=4)

r = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks', headers=headers)

tracks = r.json()

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f, ensure_ascii=False, indent=4)

audio_features = []

with open('tracks.json', 'r', encoding='utf-8') as f:
    tracks_data = json.load(f)

    for track in tracks_data["items"]:
        r = requests.get(BASE_URL + 'audio-features/' + track["track"]["id"], headers=headers)
        audio_features.append(r.json())

avg_danceability = 0
lowest_danceability = sys.float_info.max
highest_danceability = 0

avg_energy = 0
lowest_energy = sys.float_info.max
highest_energy = 0

avg_energy = 0
lowest_energy = sys.float_info.max
highest_energy = 0

keys = [0] * 12

avg_loudness = 0
lowest_loudness = -60.00
highest_loudness = 0

modes = [0] * 2

avg_speechiness = 0
lowest_speechiness = sys.float_info.max
highest_speechiness = 0

avg_acousticness = 0
lowest_acousticness = sys.float_info.max
highest_acousticness = 0

avg_instrumentalness = 0
lowest_instrumentalness = sys.float_info.max
highest_instrumentalness = 0

avg_instrumentalness = 0
lowest_instrumentalness = sys.float_info.max
highest_instrumentalness = 0

avg_liveness = 0
lowest_liveness = sys.float_info.max
highest_liveness = 0

avg_valence = 0
lowest_valence = sys.float_info.max
highest_valence = 0

for track in audio_features:
    avg_danceability += track['danceability']
    lowest_danceability = min(lowest_danceability, track['danceability'])
    highest_danceability = max(highest_danceability, track['danceability'])

    avg_energy += track['energy']
    lowest_energy = min(lowest_energy, track['energy'])
    highest_energy = max(highest_energy, track['energy'])

    keys[track['key']] += 1

    avg_loudness += track["loudness"]
    lowest_loudness = min(lowest_loudness, track['loudness'])
    highest_loudness = max(highest_loudness, track['loudness'])

    modes[track['mode']] += 1

    avg_speechiness += track["speechiness"]
    lowest_speechiness = min(lowest_speechiness, track['speechiness'])
    highest_speechiness = max(highest_speechiness, track['speechiness'])

    avg_acousticness += track["acousticness"]
    lowest_acousticness = min(lowest_acousticness, track['acousticness'])
    highest_acousticness = max(highest_acousticness, track['acousticness'])

    avg_instrumentalness += track["instrumentalness"]
    lowest_instrumentalness = min(lowest_instrumentalness, track['instrumentalness'])
    highest_instrumentalness = max(highest_instrumentalness, track['instrumentalness'])

    avg_liveness += track["liveness"]
    lowest_liveness = min(lowest_liveness, track['liveness'])
    highest_liveness = max(highest_liveness, track['liveness'])

    avg_valence += track["valence"]
    lowest_valence = min(lowest_valence, track['valence'])
    highest_valence = max(highest_valence, track['valence'])
    


    

avg_danceability = avg_danceability / len(audio_features)
avg_energy = avg_energy / len(audio_features)
avg_loudness = avg_loudness / len(audio_features)
avg_speechiness = avg_speechiness / len(audio_features)
avg_acousticness = avg_acousticness / len(audio_features)
avg_instrumentalness = avg_instrumentalness / len(audio_features)
avg_liveness = avg_liveness / len(audio_features)
avg_valence = avg_valence / len(audio_features)



