
# client_credentials_manager = SpotifyClientCredentials(client_id='f0d483d34b2c49f491f43fe5447d393a', client_secret='3d0706813c1e4e9d96e191322b2c4b9a')


import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


st.set_page_config(layout="wide")

container_style = """
    <style>
    body{
        text-align: center;
    }
        .container {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #262631;
            padding: 10px;
            border-radius: 15px;
            border: 0.5px solid gray;
            
        }
        .link-button {
            text-decoration: none;
            color: white !important;  /* Button color */
            font-weight: bold;
            # background-color: transparent !important;
            border: none !important;
            cursor: pointer;
            outline: none !important;
            
        }
        .container:hover {
            border: 1px solid white;
            border-radius: 15px;
            
        }
    </style>
"""

# Apply the CSS style
st.markdown(container_style, unsafe_allow_html=True)

# Create the container with the link button
st.markdown("""
<div class='container'>
    <a class='link-button' href='https://streamlit.io/gallery'>Log Out</a>
</div>
""", unsafe_allow_html=True)
# CSS for center-aligning the header and styling the line
page_bg_img = '''
<style>

[data-testid="stAppViewContainer"] > .main {
    background-image: url(https://i.ibb.co/w4M2kk6/img1.jpg);
 
    background-position: center;
   
    background-attachment: local, fixed;
}

</style>
'''


st.markdown(page_bg_img, unsafe_allow_html=True)

header_style = """
    <style>

     .header {
            color: #fff;
            padding: 0;
            margin-top: 0;
            text-align: center;
        }
        .caption {
            color: #fff;
            text-align: center;
            margin-top: 0;
            padding-top: 100px:
            font-size: 60px;
        }
        .line {
           
            border-bottom: 2px dashed #f85a40 #ccc;
            margin-bottom: 20px;
            padding-bottom: 80px;
        }
        .block-container st-emotion-cache-z5fcl4 ea3mdgi2 {
            padding: 0;
        }
        
        
            
    </style>
"""
# st.set_page_config(layout="wide")

# Adding the CSS to the Streamlit app
st.markdown(header_style, unsafe_allow_html=True)

# Header with center alignment and line separator
st.markdown("<h1 class='header'>The Curator<span style='color: #f85a40;'>.</span></h1>", unsafe_allow_html=True)


st.markdown("<h1 class='caption'>Music Recommendation Tool</h1>", unsafe_allow_html=True)
st.markdown("<div class='line'></div>", unsafe_allow_html=True)


# Set up Spotipy with your Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id='f0d483d34b2c49f491f43fe5447d393a', client_secret='3d0706813c1e4e9d96e191322b2c4b9a')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def recommend_music_by_artist(artist_name):
    artist = sp.search(q='artist:' + artist_name, type='artist')['artists']['items']
    if len(artist) > 0:
        artist_id = artist[0]['id']
        top_tracks = sp.artist_top_tracks(artist_id)
        tracks = []
        for track in top_tracks['tracks']:
            tracks.append({
                'name': track['name'],
                'album': track['album']['name'],
                'artists': ", ".join([artist['name'] for artist in track['artists']]),
                'release_date': track['album']['release_date'],
                'preview_url': track['preview_url'],
                'spotify_url': track['external_urls']['spotify'],  # Link to the song on Spotify
                'poster': track['album']['images'][0]['url'] if track['album']['images'] else None
            })
        return tracks
    else:
        return None

def recommend_music_by_genre(genre):
    try:
        if genre.lower() == "hip-hop":
            playlist_id = "31pj8iXJmthnqg0Qq2jPSy"  # Playlist ID for hip-hop genre
        elif genre.lower() == "rock":
            playlist_id = "0AoFXPuDaPw0JFsX8T3ZgE"  # Playlist ID for rock genre
        elif genre.lower() == "pop":
            playlist_id = "37i9dQZF1DX2vTOtsQ5Isl"  # Playlist ID for pop genre
        elif genre.lower() == "k-pop":
            playlist_id = "37i9dQZF1DX9tPFwDMOaN1"  # Playlist ID for pop genre
        elif genre.lower() == "disco":
            playlist_id = "2MIDjvystH2o9y4mPzZXUW"  # Playlist ID for pop genre
        elif genre.lower() == "phonk":
            playlist_id = "37i9dQZF1DWWY64wDtewQt"  # Playlist ID for pop genre
        elif genre.lower() == "instrumental":
            playlist_id = "1S5FWtaDXYrcpQwz1SVaxR"  # Playlist ID for pop genre
        elif genre.lower() == "jazz":
            playlist_id = "37i9dQZF1DXbITWG1ZJKYt"  # Playlist ID for jazz genre
        elif genre.lower() == "classical":
            playlist_id = "1h0CEZCm6IbFTbxThn6Xcs"  # Playlist ID for classical genre

        playlist = sp.playlist_tracks(playlist_id, limit=30)
        playlist_tracks = []
        for item in playlist['items']:
            track = item['track']
            if track is not None:
                artists = ", ".join([artist['name'] for artist in track['artists']])
                playlist_tracks.append({
                    'name': track['name'],
                    'album': track['album']['name'],
                    'artists': artists,
                    'release_date': track['album']['release_date'],
                    'preview_url': track['preview_url'],
                    'spotify_url': track['external_urls']['spotify'],  # Link to the song on Spotify
                    'poster': track['album']['images'][0]['url'] if track['album']['images'] else None
                })
        return playlist_tracks
    except spotipy.SpotifyException as e:
        st.error(f"Error occurred while fetching playlists: {e}")
        return None
    
    
def recommend_trending_top_50_global():
    try:
        playlist_id = "37i9dQZEVXbMDoHDwVN2tF"  # Playlist ID for Trending Top 50 Global
        playlist = sp.playlist_tracks(playlist_id, limit=50)
        playlist_tracks = []
        for item in playlist['items']:
            track = item['track']
            if track is not None:
                artists = ", ".join([artist['name'] for artist in track['artists']])
                playlist_tracks.append({
                    'name': track['name'],
                    'album': track['album']['name'],
                    'artists': artists,
                    'release_date': track['album']['release_date'],
                    'preview_url': track['preview_url'],
                    'spotify_url': track['external_urls']['spotify'],  # Link to the song on Spotify
                    'poster': track['album']['images'][0]['url'] if track['album']['images'] else None
                })
        return playlist_tracks
    except spotipy.SpotifyException as e:
        st.error(f"Error occurred while fetching playlists: {e}")
        return None
# Function to recommend newly released top 50 tracks
def recommend_newly_released_top_50():
    try:
        playlist_id = "37i9dQZEVXbodKHL5AS6GO"  # Playlist ID for Newly Released top 50
        playlist = sp.playlist_tracks(playlist_id, limit=50)
        playlist_tracks = []
        for item in playlist['items']:
            track = item['track']
            if track is not None:
                artists = ", ".join([artist['name'] for artist in track['artists']])
                playlist_tracks.append({
                    'name': track['name'],
                    'album': track['album']['name'],
                    'artists': artists,
                    'release_date': track['album']['release_date'],
                    'preview_url': track['preview_url'],
                    'spotify_url': track['external_urls']['spotify'],  # Link to the song on Spotify
                    'poster': track['album']['images'][0]['url'] if track['album']['images'] else None
                })
        return playlist_tracks
    except spotipy.SpotifyException as e:
        st.error(f"Error occurred while fetching playlists: {e}")
        return None
    
def Creators_choice():
    try:
        playlist_id = "5qiQEYuZkli1GH3reTcMdW"  # Playlist ID for Trending Top 50 Global
        playlist = sp.playlist_tracks(playlist_id, limit=50)
        playlist_tracks = []
        for item in playlist['items']:
            track = item['track']
            if track is not None:
                artists = ", ".join([artist['name'] for artist in track['artists']])
                playlist_tracks.append({
                    'name': track['name'],
                    'album': track['album']['name'],
                    'artists': artists,
                    'release_date': track['album']['release_date'],
                    'preview_url': track['preview_url'],
                    'spotify_url': track['external_urls']['spotify'],  # Link to the song on Spotify
                    'poster': track['album']['images'][0]['url'] if track['album']['images'] else None
                })
        return playlist_tracks
    except spotipy.SpotifyException as e:
        st.error(f"Error occurred while fetching playlists: {e}")
        return None
    
    
# User selects recommendation type
recommendation_type = st.selectbox("Select recommendation type:", ("Trending Top 50", "By Genre", "By Artist","Newly Released","Creators Choice"), key="recommendation_type")



if recommendation_type == "By Artist":
    # User provides artist name for recommendation
    artist_name = st.text_input('',placeholder='Enter Artist Name')

    if st.button("Show Tracks"):
        if artist_name.strip() == "":
            st.warning("Please enter an artist name.")
        else:
            try:
                st.write("### Recommended Tracks by", artist_name)
                recommended_tracks = recommend_music_by_artist(artist_name)
                if recommended_tracks:
                    num_tracks = len(recommended_tracks)
                    num_cols = 2  # Number of tracks in each row
                    num_rows = (num_tracks + num_cols - 1) // num_cols  # Calculate number of rows needed
                    for i in range(num_rows):
                        cols = st.columns(num_cols)
                        for j in range(num_cols):
                            index = i * num_cols + j
                            if index < num_tracks:
                                track = recommended_tracks[index]
                                with cols[j]:
                                    st.markdown(f"**{index+1}.** <span style='border: 0.3px solid #464344; border-radius: 10px; padding: 3px 5px; font-size: 20px; background-color: #464343; color: white;'>{track['name']}</span>", unsafe_allow_html=True)
                                    st.write(f"   Album: {track['album']}")
                                    st.write(f"   Release Date: {track['release_date']}")
                                    if track['poster']:
                                        # Wrap st.image() within an anchor tag
                                        st.markdown(f'<a href="{track["spotify_url"]}" target="_blank"><img src="{track["poster"]}" width="500" length="500"></a>', unsafe_allow_html=True)
                                    if track['preview_url']:
                                        # Embed audio player with custom HTML code
                                        st.write(f'<audio src="{track["preview_url"]}" controls style="width:500px"></audio>', unsafe_allow_html=True)
                                    else:
                                        st.write("No preview available for this track.")
                            if j < num_cols - 1:
                                st.markdown('<div style="margin-left: 20px;"></div>', unsafe_allow_html=True)  # Add margin between columns
                        if i < num_rows - 1:
                            st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)  # Add margin between rows
                else:
                    st.write("No tracks found for the artist.")
            except:
                st.error('Error occurred while recommending music.')
elif recommendation_type == "By Genre":
    genre = st.selectbox("Select genre:", ("Pop", "Hip-Hop", "Rock", "K-pop", "Disco", "Phonk", "Instrumental", "Jazz", "Classical"))  # Add more genres as needed
    st.write("### Recommended Tracks in", genre)
    recommended_tracks = recommend_music_by_genre(genre)
    if recommended_tracks:
        num_tracks = len(recommended_tracks)
        num_cols = 2  # Number of tracks in each row
        num_rows = (num_tracks + num_cols - 1) // num_cols  # Calculate number of rows needed
        for i in range(num_rows):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                index = i * num_cols + j
                if index < num_tracks:
                    track = recommended_tracks[index]
                    with cols[j]:
                            st.markdown(f"**{index+1}.** <span style='border: 0.3px solid #464344; border-radius: 10px; padding: 3px 5px; font-size: 20px; background-color: #464343; color: white;'>{track['name']}</span>", unsafe_allow_html=True)
                            st.write(f"   Album: {track['album']}")
                            st.write(f"   Release Date: {track['release_date']}")
                            if track['poster']:
                                # Wrap st.image() within an anchor tag
                                st.markdown(f'<a href="{track["spotify_url"]}" target="_blank"><img src="{track["poster"]}" width="500" length="500"></a>', unsafe_allow_html=True)
                            if track['preview_url']:
                                # Embed audio player with custom HTML code
                                st.write(f'<audio src="{track["preview_url"]}" controls style="width:500px"></audio>', unsafe_allow_html=True)
                            else:
                                st.write("No preview available for this track.")
                    if j < num_cols - 1:
                        st.markdown('<div style="margin-left: 20px;"></div>', unsafe_allow_html=True)  # Add margin between columns
                if i < num_rows - 1:
                    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)  # Add margin between rows
    else:
        st.write("No tracks found for the selected genre.")
elif recommendation_type == "Trending Top 50":
    st.write("### Trending Top 50 Global")
    trending_tracks = recommend_trending_top_50_global()
    if trending_tracks:
        num_tracks = len(trending_tracks)
        num_cols = 2  # Number of tracks in each row
        num_rows = (num_tracks + num_cols - 1) // num_cols  # Calculate number of rows needed
        for i in range(num_rows):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                index = i * num_cols + j
                if index < num_tracks:
                    track = trending_tracks[index]
                    with cols[j]:
                            st.markdown(f"**{index+1}.** <span style='border: 0.3px solid #464344; border-radius: 10px; padding: 3px 5px; font-size: 20px; background-color: #464343; color: white;'>{track['name']}</span>", unsafe_allow_html=True)
                            st.write(f"   Album: {track['album']}")
                            st.write(f"   Release Date: {track['release_date']}")
                            if track['poster']:
                                # Wrap st.image() within an anchor tag
                                st.markdown(f'<a href="{track["spotify_url"]}" target="_blank"><img src="{track["poster"]}" width="500" length="500"></a>', unsafe_allow_html=True)
                            if track['preview_url']:
                                # Embed audio player with custom HTML code
                                st.write(f'<audio src="{track["preview_url"]}" controls style="width:500px"></audio>', unsafe_allow_html=True)
                            else:
                                st.write("No preview available for this track.")
                    if j < num_cols - 1:
                        st.markdown('<div style="margin-left: 20px;"></div>', unsafe_allow_html=True)  # Add margin between columns
                if i < num_rows - 1:
                    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)  # Add margin between rows
    else:
        st.write("No trending tracks found.")
elif recommendation_type == "Newly Released":
    st.write("### Newly Released Top 50")
    new_tracks = recommend_newly_released_top_50()
    if new_tracks:
        num_tracks = len(new_tracks)
        num_cols = 2  # Number of tracks in each row
        num_rows = (num_tracks + num_cols - 1) // num_cols  # Calculate number of rows needed
        for i in range(num_rows):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                index = i * num_cols + j
                if index < num_tracks:
                    track = new_tracks[index]
                    with cols[j]:
                            st.markdown(f"**{index+1}.** <span style='border: 0.3px solid #464344; border-radius: 10px; padding: 3px 5px; font-size: 20px; background-color: #464343; color: white;'>{track['name']}</span>", unsafe_allow_html=True)
                            st.write(f"   Album: {track['album']}")
                            st.write(f"   Release Date: {track['release_date']}")
                            if track['poster']:
                                # Wrap st.image() within an anchor tag
                                st.markdown(f'<a href="{track["spotify_url"]}" target="_blank"><img src="{track["poster"]}" width="500" length="500"></a>', unsafe_allow_html=True)
                            if track['preview_url']:
                                # Embed audio player with custom HTML code
                                st.write(f'<audio src="{track["preview_url"]}" controls style="width:500px"></audio>', unsafe_allow_html=True)
                            else:
                                st.write("No preview available for this track.")
                    if j < num_cols - 1:
                        st.markdown('<div style="margin-left: 20px;"></div>', unsafe_allow_html=True)  # Add margin between columns
                if i < num_rows - 1:
                    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)  # Add margin between rows
    else:
        st.write("No newly released tracks found.")
elif recommendation_type == "Creators Choice":
    st.write("### Creators choice")
    creator_tracks = Creators_choice()
    if creator_tracks:
        num_tracks = len(creator_tracks)
        num_cols = 2  # Number of tracks in each row
        num_rows = (num_tracks + num_cols - 1) // num_cols  # Calculate number of rows needed
        for i in range(num_rows):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                index = i * num_cols + j
                if index < num_tracks:
                    track = creator_tracks[index]
                    with cols[j]:
                            st.markdown(f"**{index+1}.** <span style='border: 0.3px solid #464344; border-radius: 10px; padding: 3px 5px; font-size: 20px; background-color: #464343; color: white;'>{track['name']}</span>", unsafe_allow_html=True)
                            st.write(f"   Album: {track['album']}")
                            st.write(f"   Release Date: {track['release_date']}")
                            if track['poster']:
                                # Wrap st.image() within an anchor tag
                                st.markdown(f'<a href="{track["spotify_url"]}" target="_blank"><img src="{track["poster"]}" width="500" length="500"></a>', unsafe_allow_html=True)
                            if track['preview_url']:
                                # Embed audio player with custom HTML code
                                st.write(f'<audio src="{track["preview_url"]}" controls style="width:500px"></audio>', unsafe_allow_html=True)
                            else:
                                st.write("No preview available for this track.")
                    if j < num_cols - 1:
                        st.markdown('<div style="margin-left: 20px;"></div>', unsafe_allow_html=True)  # Add margin between columns
                if i < num_rows - 1:
                    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)  # Add margin between rows
    else:
        st.write("No trending tracks found.")