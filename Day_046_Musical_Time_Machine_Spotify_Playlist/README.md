# Day_046_Musical_Time_Machine_Spotify_Playlist

This project is part of my 100 Days of Code journey.

## Project Description

On Day 46, the focus was on building a **Musical Time Machine** that creates a Spotify playlist of the Billboard Hot 100 songs from a specific date in the past. This project combined **web scraping** with **API integration**, covering:

1. **Web Scraping (Beautiful Soup & Requests):** Fetching the Billboard Hot 100 chart from a user-specified date using `requests` and parsing the HTML with `BeautifulSoup` to extract song titles.
    
2. **Spotify API Integration (Spotipy):**
    
    - **OAuth 2.0 Authentication:** Authenticating with the Spotify API to get user permissions (e.g., to create playlists).
        
    - **Searching for Tracks:** Using the Spotify API to search for the extracted song titles and retrieve their Spotify URIs.
        
    - **Creating Playlists:** Programmatically creating a new private Spotify playlist.
        
    - **Adding Tracks to Playlist:** Adding the found song URIs to the newly created playlist.
        
3. **Date Handling:** Taking a date input from the user and formatting it correctly for both the Billboard URL and Spotify API calls.
    

The application allows you to "travel back in time" to a specific date, discover what songs were popular then, and automatically generate a Spotify playlist of those tracks.

## How to Run

This project requires you to set up a Spotify Developer account and create an application to get your Client ID and Client Secret. You'll also need to configure a Redirect URI.

1. **Spotify Developer Setup:**
    
    - Go to [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard/applications "null").
        
    - Log in with your Spotify account.
        
    - Click "Create an app."
        
    - Fill in the details (App Name, Description).
        
    - After creation, find your **Client ID** and **Client Secret**.
        
    - Go to "Edit Settings" for your app. Add `http://example.com` (or any valid URL you control, though `http://example.com` is commonly used for local development with `spotipy`) as a **Redirect URI**. This URI doesn't need to host anything; it's just where Spotify redirects after authentication.
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_046_Musical_Time_Machine_Spotify_Playlist
    ```
    
4. **Install Required Libraries:**
    
    ```
    pip install requests beautifulsoup4 spotipy
    ```
    
5. **Configure Credentials:** Open the `main.py` file and replace the placeholder values for `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` with your actual Spotify app credentials.
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

When you run the script, it will first ask you for a date. It will then open a browser window (or provide a URL to copy) for Spotify authentication. You'll need to authorize your app and then copy the redirected URL back into your console. After successful authentication, it will scrape the Billboard chart for the specified date, search for the songs on Spotify, create a new playlist (e.g., "YYYY-MM-DD Billboard 100"), and add the found tracks.

```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
1995-12-25
# (Browser window opens for Spotify authentication)
Please paste the redirect URL here:
http://example.com/?code=AQB... (paste the full URL from your browser here)

# (Console output will show progress)
Searching for songs on Spotify...
Found 'One Sweet Day' by Mariah Carey & Boyz II Men.
Found 'Exhale (Shoop Shoop)' by Whitney Houston.
... (continues for all 100 songs)
Creating playlist '1995-12-25 Billboard 100'...
Adding songs to playlist...
Playlist created successfully! You can find it in your Spotify account.
```

## Concepts Learned

- **Web Scraping (Advanced):** Extracting specific data points from complex HTML structures.
    
- **API Integration (Spotify):** Working with a popular and well-documented API.
    
- **OAuth 2.0 Flow:** Understanding the basics of user authentication for third-party services.
    
- **`spotipy` Library:** Using a Python wrapper for the Spotify API to simplify interactions.
    
- **Data Matching:** Bridging data from web scraping (song titles) to API searches.
    
- **Playlist Management:** Programmatically creating and populating playlists.
    
- **Error Handling:** Gracefully handling cases where songs might not be found on Spotify.

## Author

[Musn0o](https://github.com/Musn0o)