from django.shortcuts import render
import sys
import os
import platform

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from combine import download_playlist  # Import the correct function from combine.py

def get_music_folder():
    # Get the path to the user's Music folder
    if platform.system() == "Windows":
        return os.path.join(os.path.expanduser("~"), "Music")
    elif platform.system() == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Music")
    else:  # Linux or other OS
        return os.path.join(os.path.expanduser("~"), "Music")

def index(request):
    download_message = ""
    if request.method == 'POST':
        input_term = request.POST.get('input_term')

        # Ensure input_term is passed to the download_playlist function
        if input_term:
            try:
                download_playlist(input_term)  # Pass input_term as argument
                download_message = "Download successful!"
            except Exception as e:
                download_message = f"Error during download: {e}"
        else:
            download_message = "Please provide a valid link."

    return render(request, 'downloader/index.html', {'download_message': download_message})
