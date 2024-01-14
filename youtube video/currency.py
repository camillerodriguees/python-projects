from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully")

    except Exception as e:
        print(e)

def open_file_dialog(entry_var):
    folder = filedialog.askdirectory()
    if folder:
        entry_var.set(folder)
        print(f"Selected folder: {folder}")

def start_download(entry_url, entry_save_dir):
    video_url = entry_url.get()
    save_dir = entry_save_dir.get()

    if video_url and save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid input. Please provide both URL and save location.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Video Downloader")

    # Variável de controle para a entrada do diretório
    save_dir_var = tk.StringVar()

    # Criando widgets
    label_url = tk.Label(root, text="YouTube URL:")
    entry_url = tk.Entry(root, width=40)

    label_save_dir = tk.Label(root, text="Save Directory:")
    entry_save_dir = tk.Entry(root, textvariable=save_dir_var, width=30)
    button_browse = tk.Button(root, text="Browse", command=lambda: open_file_dialog(save_dir_var))

    button_download = tk.Button(root, text="Download", command=lambda: start_download(entry_url, entry_save_dir))

    # Organizando os widgets na tela
    label_url.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_url.grid(row=0, column=1, columnspan=2, pady=5)

    label_save_dir.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_save_dir.grid(row=1, column=1, pady=5)
    button_browse.grid(row=1, column=2, pady=5)

    button_download.grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()
