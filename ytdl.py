import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_downloader(mode):
    # Get links
    raw_text = url_text.get("1.0", tk.END)
    links = [line.strip() for line in raw_text.splitlines() if line.strip()]

    if not links:
        messagebox.showerror("Error", "Please paste at least one YouTube link!")
        return

    download_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Wrap each URL in quotes
    url_args = " ".join(links)

    if mode == "audio":
        command = (
            f'yt-dlp -x --audio-format mp3 '
            f'-P "{download_path}" '
            f'{url_args} '
            f'& echo. '
            f'& echo All downloads complete! '
            f'& timeout /t 5'
        )
    else:
        command = (
            f'yt-dlp '
            f'-P "{download_path}" '
            f'{url_args} '
            f'& echo. '
            f'& echo All downloads complete! '
            f'& timeout /t 5'
        )

    try:
        subprocess.Popen(["cmd", "/k", command])
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "Command Prompt could not be opened."
        )


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Goblin Downloader (Windows)")
root.geometry("500x300")
root.resizable(False, False)

lbl = tk.Label(
    root,
    text="Paste YouTube Links (One per line):",
    font=("Arial", 12, "bold")
)
lbl.pack(pady=(15, 5))

url_text = tk.Text(
    root,
    height=8,
    width=55,
    font=("Arial", 10)
)
url_text.pack(padx=10, pady=5)

btn_audio = tk.Button(
    root,
    text="Download MP3s (Audio)",
    bg="#d1e7dd",
    font=("Arial", 10, "bold"),
    command=lambda: run_downloader("audio")
)
btn_audio.pack(fill="x", padx=50, pady=(10, 5))

btn_video = tk.Button(
    root,
    text="Download MP4s (Video)",
    bg="#cfe2ff",
    font=("Arial", 10),
    command=lambda: run_downloader("video")
)
btn_video.pack(fill="x", padx=50, pady=5)

root.mainloop()