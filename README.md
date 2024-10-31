
# Spotify Top Indonesian Tracks EDA

This project provides an exploratory data analysis (EDA) of the top Indonesian tracks on Spotify for October 2024. Using **Spotipy** to access Spotify’s API and **Streamlit** for visualization, the app offers insights into track popularity, album, artist frequency, and more.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

## Features
- Retrieves the latest top 50 tracks in Indonesia using Spotify’s API.
- Displays track data including name, artist, popularity, album, and release date.
- Visualizes:
  - Track popularity distribution in Indonesia.
  - Most frequently featured artists among the top 50 tracks.

## Setup

### Prerequisites
- **Python 3.7+** is required.
- **Spotify Developer Account**: You’ll need to create a Spotify Developer account to get `client_id` and `client_secret` values for accessing Spotify’s API.

### Spotify Developer Credentials
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
2. Create a new application.
3. Copy the `Client ID` and `Client Secret` for use in the app.

### Environment Variables
In the project root, create a `.env` file with the following values:
```plaintext
SPOTIPY_CLIENT_ID='your_client_id'
SPOTIPY_CLIENT_SECRET='your_client_secret'
```

## Installation

Clone this repository and install dependencies:
```bash
git clone https://github.com/leerizza/eda-spotify-indonesian-songs.git
cd eda-spotify-indonesian-songs
```

### Install Python Dependencies
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Getting Started

1. **Run the Streamlit App**:
   ```bash
   streamlit run eda-spotify-indonesian-songs.py
   ```
2. **Access the Application**:
   After starting the app, open the local URL (usually `http://localhost:8501`) in your web browser to explore the data.

## Usage

### Main Functionalities
1. **Top Tracks Data Table**: View the table of the top 50 tracks in Indonesia, with columns for:
   - `Name`: Track name
   - `Artist`: Main artist
   - `Popularity`: Spotify’s popularity metric
   - `Album`: Album name
   - `Release Date`: Release date of the track’s album
2. **Track Popularity Distribution**: View the histogram showing the popularity distribution across top tracks.
3. **Most Featured Artists**: A bar chart displays the most frequent artists in the top 50 tracks list.

### Sample Code Snippet for API Call and Displaying Data
```python
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import altair as alt

# Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Function to get top 50 tracks from Indonesia playlist
def get_top_tracks():
    results = sp.playlist_tracks(playlist_id="37i9dQZEVXbObFQZ3JLcXt")  # Replace with Indonesian playlist ID
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity'],
            'album': track['album']['name']
        })
    return pd.DataFrame(tracks)

# Display top tracks
top_tracks_df = get_top_tracks()
st.write("### Top Indonesian Tracks - October 2024")
st.dataframe(top_tracks_df)
```

### Example Output
- **Data Table**: A table showing track details such as name, artist, popularity, album, and release date.
- **Popularity Distribution Chart**: A histogram visualizing the popularity range.
- **Artist Frequency Chart**: A bar chart showing the most featured artists in the top 50 tracks.

## Project Structure
```
spotify-top-tracks-eda/
│
├── app.py                   # Main Streamlit app script
├── README.md                # Documentation
├── requirements.txt         # Dependencies list
├── .env                     # Environment variables (Spotify credentials)
└── data/                    # (Optional) Folder to save fetched data
```

## Acknowledgments
- **Spotify** for providing the API to access music data.
- **Streamlit** for enabling rapid development of a user-friendly dashboard.
- **Spotipy** for simplifying interactions with the Spotify API.
