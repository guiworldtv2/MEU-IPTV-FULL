import os
import streamlink
import subprocess
import time

url = "https://5a7d54e35f9d2.streamlock.net/avt7/avt7.stream/chunklist_w127968702.m3u8"
stream = streamlink.streams(url)["best"]

while True:
    filename = time.strftime("%Y-%m-%d_%H-%M-%S.png")
    subprocess.call(["ffmpeg", "-i", stream.url, "-vframes", "1", filename])
    time.sleep(30)
