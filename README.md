# music.py
 Music Player

## Installation of the Music.py Project

This project allows you to set up a Spotify API integration to fetch songs from a specified playlist and write them in a format of your choice. To get started with this project, follow the installation steps below.

### Prerequisites

Before using the project, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

**You can download for windows without python [here](https://github.com/milosnowcat/music.py/releases/latest)!**

1. Clone the GitHub repository containing the Music.py project to your local machine using the following command:

   ```bash
   git clone https://github.com/milosnowcat/music.py.git
   ```

2. Navigate to the `music.py` directory:

   ```bash
   cd music.py
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the `main.py` script:

   ```bash
   python main.py
   ```

5. The script will prompt you to set up your Spotify API credentials, including Client ID, Client Secret, Redirect URI, Spotify username, and Playlist ID.

6. You can also set the format for writing the songs (default is "/play").

7. The script will count down and start writing the songs from the specified playlist in the chosen format.

8. To stop the script, press `Ctrl + C` in your terminal.

That's it! You have successfully installed and used the Music.py project to fetch and write songs from a Spotify playlist.

---

## Using the Music.py Project

The Music.py project allows you to set up a Spotify API integration to fetch songs from a specified playlist and write them in a format of your choice. Follow these steps to use the project.

### Setting up Spotify API Credentials

1. Ensure you have followed the installation steps mentioned in the "Installation of the Music.py Project" section.

2. Run the `main.py` script:

   ```bash
   python main.py
   ```

3. The script will prompt you to set up your Spotify API credentials:
   - Client ID: Your Spotify API client ID obtained from the Spotify Developer platform.
   - Client Secret: The confidential string for authenticating your application.
   - Redirect URI: The URI where the user is redirected after granting permission to access their Spotify account.
   - Spotify Username: Your Spotify username.
   - Playlist ID: The unique identifier for the playlist you want to fetch.

4. You can also set the format for writing the songs (default is "/play").

5. The script will count down and start writing the songs from the specified playlist in the chosen format.

6. To stop the script, press `Ctrl + C` in your terminal.

That's it! You have successfully used the Music.py project to fetch and write songs from a Spotify playlist using your Spotify API credentials.
