import streamlink
import moviepy.editor as mp
import subprocess
import os
import time

# URL do stream
url = "https://5a7d54e35f9d2.streamlock.net/avt7/avt7.stream/chunklist_w127968702.m3u8"

# Tempo de captura de cada frame (em segundos)
capture_time = 5

# Número de frames a serem capturados
num_frames = 60

# Iniciar o stream
streams = streamlink.streams(url)
stream = streams["best"]

# Iniciar a captura de frames
for i in range(num_frames):
    filename = "frame_{}.png".format(i)
    subprocess.call(["ffmpeg", "-i", stream.url, "-vframes", "1", filename])
    time.sleep(capture_time)

# Criar o vídeo a partir dos frames capturados
filenames = ["frame_{}.png".format(i) for i in range(num_frames)]
clip = mp.ImageSequenceClip(filenames, fps=1 / capture_time)
clip.write_videofile("timelapse.mp4")

# Limpar os arquivos de frame
for filename in filenames:
    os.remove(filename)

   
