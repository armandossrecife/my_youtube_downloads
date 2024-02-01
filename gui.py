import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os

class MainWindow:
    def __init__(self, my_app, my_title):
        # App Frame
        self.app = my_app
        self.app.title(my_title)

        # Add UI elements
        self.url_label = tk.Label(self.app, text="Enter YouTube video URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(self.app, width=50)
        self.url_entry.pack(padx=5, pady=5,fill = tk.BOTH)
        self.download_button = tk.Button(self.app, text="Download", command=self.download_video)
        self.download_button.pack()
        self.finish_label = tk.Label(self.app, text="")
        self.finish_label.pack()
        self.p_percentage = tk.Label(self.app, text="0%")
        self.p_percentage.pack()
        self.progress_bar = tk.ttk.Progressbar(self.app, orient="horizontal", length=300, mode="determinate")
        self.progress_bar['value'] = 0
        self.progress_bar.pack(padx=5, pady=5,fill = tk.BOTH)
        self.scrollbar = tk.Scrollbar(self.app)
        self.download_history_list = tk.Listbox(self.app, width=40, height=10, yscrollcommand=self.scrollbar.set)  # Use a Listbox for simplicity        
        self.scrollbar.config(command = self.download_history_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.download_history_list.pack(padx=5, pady=5,fill=tk.BOTH, expand=True)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = (bytes_downloaded/total_size)*100
        percentage = str(int(percentage_of_completion))
        self.p_percentage.config(text=percentage + '%')
        self.p_percentage.update_idletasks()
        print(percentage + '%')
        self.progress_bar['value'] = float(percentage_of_completion)
        self.progress_bar.update_idletasks()

    def on_complete(self, stream, file_path):
        print("Download complete:", file_path)
        self.finish_label.config(text="Download complete")
        self.p_percentage.config(text='100%')
        self.p_percentage.update_idletasks()
        self.progress_bar['value'] = 100
        self.progress_bar.update_idletasks()
        # Perform other actions as needed (e.g., play a sound, update download history)

    # Function to download a video
    def download_video(self):
        try:
            url = self.url_entry.get()
            if len(url) == 0:
                raise ValueError('URL Vazia!')
            print(self.download_history_list.get(0, tk.END))
            print('Faz o download...')
            self.progress_bar['value'] = 0
            self.progress_bar.update_idletasks()
            self.finish_label.config(text='Aguarde...')
            self.finish_label.update_idletasks()
            self.p_percentage.config(text='0%')
            self.p_percentage.update_idletasks()
            yt = YouTube(url, on_progress_callback=self.on_progress, on_complete_callback=self.on_complete)
            os.makedirs("videos", exist_ok=True)  # Create the "videos" folder if needed
            stream = yt.streams.get_highest_resolution()  # Or any other chosen stream
            stream.download(output_path="videos")
            # Add video to download history
            self.download_history_list.insert(tk.END, yt.title)
        except ValueError as ve: 
            print(f'Erro: {str(ve)}')
            self.finish_label.config(text=f'{str(ve)}')
        except Exception as ex:
            print("Error:", ex)
            # Display error message to the user (optional)
            self.finish_label.config(text=f'Erro no download: {str(ex)}')