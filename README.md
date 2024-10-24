# 🎵 Music Downloader Web App

## Overview
This **Music Downloader Web App** allows users to download audio from YouTube and Spotify directly from a simple and intuitive web interface. Enter a YouTube or Spotify playlist link, or a search term, and the app will find the best match and download the audio files as MP3s.

The project utilizes Python's powerful libraries like `yt_dlp` and the YouTube API to handle YouTube videos, as well as `spotipy` for accessing and fetching Spotify playlist details. This application is built using **Django** for the backend and **Bootstrap** for a responsive and user-friendly frontend.

## Features
- **Download YouTube Videos or Playlists**: Provide a YouTube video or playlist link, and the app will download audio in high quality.
- **Spotify Playlist Support**: Enter a Spotify playlist link to search for corresponding YouTube tracks and download them.
- **Search Functionality**: Enter a search term, and the app will find the closest matching video on YouTube to download.
- **User-Friendly Notifications**: The app displays notifications on successful downloads, which disappear after 5 seconds (unless hovered over).
- **Responsive Design**: Frontend is powered by Bootstrap, offering a clean and responsive user interface.
- **Folder Organization**: Downloads are saved directly into a custom-named folder based on the playlist name in your system’s Music directory.

## Tech Stack
- **Backend**: Django, Python
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **APIs**:
  - YouTube Data API v3 for fetching video and playlist details
  - Spotipy (Spotify Web API wrapper) for handling Spotify playlists
- **Download Library**: `yt_dlp` for downloading YouTube audio

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/music-downloader-webapp.git
   cd music-downloader-webapp
  `
2.Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3.Set up your environment:

Create a .env file for your YouTube API key and Spotify credentials.

4.Run the Django app:
```bash
python manage.py runserver
```
5.Access the app at http://localhost:8000.

## Future Enhancements
- Add support for more streaming services like SoundCloud.
- Implement user authentication and personalized download history.
- Enable batch downloading.

Thank you! 

