import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os # Used for environment variables, though direct assignment is used here for simplicity

# --- Configuration ---

# Billboard Hot 100 URL base
BILLBOARD_URL_BASE = "https://www.billboard.com/charts/hot-100/"

# Spotify API Credentials
# Get these from your Spotify Developer Dashboard: https://developer.spotify.com/dashboard/applications
# Create an app, then copy your Client ID and Client Secret.
# Add "http://example.com" (or your chosen URL) to your Redirect URIs in app settings.
SPOTIPY_CLIENT_ID = "YOUR_SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_SPOTIPY_CLIENT_SECRET"
SPOTIPY_REDIRECT_URI = "http://example.com" # Must match one of your app's Redirect URIs

# Spotify API Scope - defines what permissions your app needs
# 'playlist-modify-private' allows creating and modifying private playlists.
SPOTIPY_SCOPE = "playlist-modify-private"

# --- User Input ---
# Get the date from the user for the "time travel"
travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

# --- Web Scraping Billboard Hot 100 ---
# Construct the full URL for the Billboard chart on the specified date
billboard_url = f"{BILLBOARD_URL_BASE}{travel_date}"

print(f"Fetching Billboard Hot 100 for {travel_date}...")
try:
    response = requests.get(billboard_url)
    response.raise_for_status() # Raise an exception for bad status codes
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all song titles. The exact CSS selector might change over time,
    # so inspect Billboard's page if this selector stops working.
    # This selector targets h3 tags with specific classes that contain song titles.
    song_titles_html = soup.select("li ul li h3.c-title")
    song_titles = [title.getText().strip() for title in song_titles_html]

    if not song_titles:
        print("Could not find any song titles. Check the Billboard URL or selector.")
        exit()

    print(f"Found {len(song_titles)} songs from {travel_date}.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching Billboard data: {e}")
    print("Please check the URL or your internet connection.")
    exit()
except Exception as e:
    print(f"An error occurred during web scraping: {e}")
    exit()

# --- Spotify Authentication ---
# This part handles the OAuth 2.0 authorization flow.
# Spotipy will open a browser window for you to log in and authorize the app.
# After authorization, Spotify will redirect to SPOTIPY_REDIRECT_URI with an authorization code.
# Spotipy then captures this code to get an access token.

sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SPOTIPY_SCOPE,
    show_dialog=True, # Forces re-authentication every time, useful for development
    cache_path="token.txt" # Cache token for future use, optional
)

# This line will open a browser window for authentication.
# The user needs to complete the authentication in the browser and then
# paste the redirected URL back into the console.
print("\nOpening browser for Spotify authentication. Please authorize the app.")
print("After authorization, copy the full URL from your browser and paste it here:")
token_info = sp_oauth.get_access_token(as_dict=False) # as_dict=False returns the token directly
# The above line will block until the user pastes the URL or manually closes the browser.

# Initialize Spotipy client with the authenticated token
sp = spotipy.Spotify(auth=token_info) # Use auth=token_info for direct token use

# Get the current user's ID
user = sp.current_user()
if user is None or "id" not in user:
    print("Error: Could not retrieve Spotify user information. Check your authentication.")
    exit()
user_id = user["id"]
print(f"Authenticated as Spotify user: {user_id}")

# --- Search for Songs on Spotify and Collect URIs ---
song_uris = []
year = travel_date.split("-")[0] # Extract the year from the date

print("\nSearching for songs on Spotify...")
for song_title in song_titles:
    try:
        # Search for the song, limiting results to the specific year for better accuracy
        result = sp.search(q=f"track:{song_title} year:{year}", type="track")
        # If tracks are found, get the URI of the first (most relevant) one
        if result and "tracks" in result and "items" in result["tracks"] and result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            # print(f"Found '{song_title}' by {result['tracks']['items'][0]['artists'][0]['name']}.")
        else:
            print(f"'{song_title}' not found on Spotify.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error searching for '{song_title}' on Spotify: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while searching for '{song_title}': {e}")

# --- Create a New Spotify Playlist ---
playlist_name = f"{travel_date} Billboard 100"
playlist_description = f"Billboard Hot 100 songs from {travel_date}"

print(f"\nCreating playlist '{playlist_name}'...")
try:
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)
    if playlist is None or "id" not in playlist:
        print("Error: Could not create playlist. Check your Spotify credentials and permissions.")
        exit()
    playlist_id = playlist["id"]
    print(f"Playlist '{playlist_name}' created successfully! ID: {playlist_id}")
except spotipy.exceptions.SpotifyException as e:
    print(f"Error creating playlist: {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while creating playlist: {e}")
    exit()

# --- Add Songs to the Playlist ---
if song_uris:
    print("Adding songs to playlist...")
    try:
        # Spotify API allows adding up to 100 tracks per request
        sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
        print("Songs added to playlist successfully!")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error adding songs to playlist: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while adding songs: {e}")
else:
    print("No songs found to add to the playlist.")

print("\nPlaylist creation process complete. Check your Spotify account!")

