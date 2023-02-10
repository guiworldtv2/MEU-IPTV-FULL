import streamlink
import moviepy.editor as mp
import subprocess
import os
import time

# URL do stream
url = "https://hunq9fz8yk.zoeweb.tv/flamboyant/flamboyant.stream/chunklist.m3u8"

# Tempo de captura de cada frame (em segundos)
capture_time = 5

# Número de frames a serem capturados
num_frames = 120

# Duração do vídeo final (em segundos)
video_duration = 400

# Taxa de quadros por segundo (FPS) da timelapse
fps = 30

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
clip = mp.ImageSequenceClip(filenames, fps=fps)

# Ajustar a duração do vídeo
clip = clip.set_duration(video_duration)

# Exportar o vídeo
clip.write_videofile("timelapse2.mp4", preset='ultrafast', fps=fps)

# Limpar os arquivos de frame
for filename in filenames:
    os.remove(filename)

# Baixar e salvar apenas o áudio do vídeo de exemplo
subprocess.call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "https://www.youtube.com/watch?v=RfYmwwQnPR8"])

