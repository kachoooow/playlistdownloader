import os
import yt_dlp

def download_playlist(playlist_url, download_folder):
    # Create download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'format': 'best'
    }
    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print('Download complete')

if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL : ")
    if not playlist_url.strip():
        playlist_url = "https://www.youtube.com/playlist?list=PLWUuMxUJvnuKDF9DncRGZPKssW0G7uyLi"

    download_folder = input("Enter the download folder path : ")
    if not download_folder.strip():
        download_folder = "C:/Users/User/Desktop/vsc/New folder/muska"

    download_playlist(playlist_url, download_folder)