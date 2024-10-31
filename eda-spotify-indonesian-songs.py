import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import altair as alt

# Spotify credentials
client_id = "7c4bd0e14e8d4d21b069c07050978f7e"
client_secret = "c53a0cfa11004ed58ad0938a1175844e"

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Fetch the top 50 tracks in Indonesia
def get_top_tracks():
    results = sp.playlist_tracks(playlist_id="37i9dQZEVXbObFQZ3JLcXt")  # Replace with appropriate playlist ID for Indonesia's top songs
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity'],
            'album': track['album']['name'],
            'preview_url': track.get('preview_url')
        })
    return pd.DataFrame(tracks)

# Dataframe of top tracks
top_tracks_df = get_top_tracks()

# Streamlit App
st.title("Spotify Top Indonesian Tracks - October 2024")
st.subheader("Exploratory Data Analysis of Top Tracks")

# Display data table
st.write("### Top Tracks Data")
st.dataframe(top_tracks_df)

# Popularity Chart
st.write("### Track Popularity Distribution")
popularity_chart = alt.Chart(top_tracks_df).mark_bar().encode(
    x=alt.X('popularity', bin=alt.Bin(maxbins=30), title='Popularity Score'),
    y='count()',
    color='artist'
).properties(title="Popularity Distribution of Top Tracks in Indonesia")

st.altair_chart(popularity_chart, use_container_width=True)

# Artist Frequency
st.write("### Most Featured Artists")
artist_count = top_tracks_df['artist'].value_counts().reset_index()
artist_count.columns = ['artist', 'count']
artist_chart = alt.Chart(artist_count.head(10)).mark_bar().encode(
    x='count',
    y=alt.Y('artist', sort='-x')
).properties(title="Top Artists in Indonesian Top Tracks")

st.altair_chart(artist_chart, use_container_width=True)

 # Display Track Previews
st.write("### Track Previews")
for index, row in top_tracks_df.iterrows():
        if row['preview_url']:
            st.write(f"**{row['name']}**")
            st.audio(row['preview_url'])
        else:
            st.write(f"**{row['name']}** - No preview available.")
else:
    st.write("No data found. Please check the artist name.")