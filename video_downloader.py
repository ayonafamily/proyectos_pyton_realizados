import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox



def descargar_videos(url, status_label):
    if not url:
        messagebox.showerror("Error", "URL inválida")
        return
    
    status_label.config(text="Descargando...")
    
    directorio_actual = os.getcwd()
    directorio_videos = "/home/jorge/Vídeos"
    
    if directorio_actual != directorio_videos:
        os.chdir(directorio_videos)
                       
    subprocess.call(["yt-dlp", url])
    status_label.config(text="Descarga completada")

def main():
    root = tk.Tk()
    root.title("Descargar videos")

    label = tk.Label(root, text="Ingrese la URL del video:")
    label.pack()

    url_entry = tk.Entry(root)
    url_entry.pack()

    status_label = tk.Label(root, text="")
    status_label.pack()

    def on_download():
        url = url_entry.get()
        descargar_videos(url, status_label)

    download_button = tk.Button(root, text="Descargar", command=on_download)
    download_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
