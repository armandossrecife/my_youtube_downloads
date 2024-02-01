# My Video Downloader

The prototype of Downloader application

# Requirements

Here are the main features and requirements for a desktop application that downloads videos from YouTube:

## Essential Features:

- **YouTube URL pasting**: Allow users to paste YouTube video URLs directly into the app.
- **Video format selection**: Offer choices for video format (MP4, AVI, etc.) and quality (720p, 1080p, etc.).
- **Audio extraction**: Provide the option to download videos as audio-only files (MP3, WAV, etc.).
- **Download progress bar**: Display a progress bar to track download status.
- **Download management**: Allow users to pause, resume, and cancel downloads.
- **Download history**: Maintain a list of downloaded videos for easy access.

## Additional Features (to enhance user experience):

- **Playlist download**: Enable downloading entire playlists or multiple videos at once.
- **Subtitle download**: Allow downloading subtitles in various languages.
- **Batch download**: Facilitate downloading multiple videos simultaneously.
- **Search functionality**: Integrate a search bar to find videos directly within the app.
- **Customizable settings**: Offer options for default download location, language, and theme.

## Technical Requirements:

- **YouTube API interaction**: Integrate with YouTube's API to fetch video information and download links.
- **Video download libraries**: Utilize libraries like FFmpeg or pytube for video downloading and processing.
- **GUI development**: Choose a suitable GUI framework (e.g., Qt, Tkinter, Electron) for the application's interface.
- **Cross-platform compatibility**: Consider making the app compatible with multiple operating systems (Windows, macOS, Linux).
- **Regular updates**: Stay updated with YouTube's API changes and address any compatibility issues.

## Legal Considerations:

- **YouTube's Terms of Service**: Adhere to YouTube's terms regarding video downloading to avoid violating copyright laws.
- **Inform users**: Clearly inform users about the legal implications of downloading videos and their responsibility to respect copyright.

# My Protype 

## GUI Framework

Tkinter (built-in with Python): Simple and beginner-friendly.

## Instalation

- Ensure you have Python installed (https://www.python.org/downloads/).
- Install PyTube using pip: 

```bash
pip install pytube
```
- Ensure you have tkinter in your system

Obs: Fix tkinter in your OS (Operating System): https://stackoverflow.com/questions/25905540/importerror-no-module-named-tkinter

## Run main application

```bash
python3 main.py
```
![Main window](https://github.com/armandossrecife/my_videos/blob/main/main.png)




