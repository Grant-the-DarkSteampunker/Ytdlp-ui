import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_downloader(mode):
    # Get text from line 1, character 0 to the end
    raw_text = url_text.get("1.0", tk.END)
    
    # Split the text by new lines to get individual links
    links = [line.strip() for line in raw_text.split('\n') if line.strip()]
    
    if not links:
        messagebox.showerror("Error", "Please paste at least one YouTube link!")
        return

    # Define the Downloads folder path
    download_path = os.path.expanduser("~/Downloads")
    
    # Create a single string of all URLs wrapped in quotes
    # e.g. 'link1' 'link2' 'link3'
    url_args = " ".join([f"'{link}'" for link in links])
    
    # Base command to open terminal
    cmd = ["x-terminal-emulator", "-e"]
    
    # Construct the yt-dlp command string
    # It will process all links in the url_args list sequentially
    if mode == "audio":
        bash_command = f"yt-dlp -x --audio-format mp3 -P '{download_path}' {url_args}; echo 'All Done! Closing in 5 seconds...'; sleep 5"
    else:
        bash_command = f"yt-dlp -P '{download_path}' {url_args}; echo 'All Done! Closing in 5 seconds...'; sleep 5"

    # Final command structure
    full_command = cmd + ["bash", "-c", bash_command]

    try:
        subprocess.Popen(full_command)
    except FileNotFoundError:
        messagebox.showerror("Error", "Could not open terminal.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Goblin Downloader (Multi-Link)")
root.geometry("500x300") # Made the window bigger
root.resizable(False, False)

# Label
lbl = tk.Label(root, text="Paste Links (One per line):", font=("Arial", 12, "bold"))
lbl.pack(pady=(15, 5))

# Text Box (Multiline)
url_text = tk.Text(root, height=8, width=55, font=("Arial", 10))
url_text.pack(pady=5, padx=10)

# Audio Button
btn_audio = tk.Button(root, text="Download MP3s (Audio)", bg="#d1e7dd", font=("Arial", 10, "bold"), command=lambda: run_downloader("audio"))
btn_audio.pack(pady=(10, 5), fill="x", padx=50)

# Video Button
btn_video = tk.Button(root, text="Download MP4s (Video)", bg="#cfe2ff", font=("Arial", 10), command=lambda: run_downloader("video"))
btn_video.pack(pady=5, fill="x", padx=50)

# Start the app
root.mainloop()
