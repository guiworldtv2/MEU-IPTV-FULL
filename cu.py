import streamlink
import moviepy.editor as mp
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
frames = []
for i in range(num_frames):
    frame = stream.get_frames()
    frames.append(frame)
    time.sleep(capture_time)

# Criar o vídeo a partir dos frames capturados
clip = mp.ImageSequenceClip(frames, fps=1 / capture_time)
clip.write_videofile("timelapse.mp4")
