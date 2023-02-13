import time
import os
import subprocess
from selenium import webdriver
from bs4 import BeautifulSoup

while True:
    try:
        # URL da página desejada
        url_youtube = "https://www.youtube.com/results?search_query=aula&sp=CAISBBABGAI%253D"

        # Instanciando o driver do firefox
        driver = webdriver.Firefox()

        # Abrir a página desejada
        driver.get(url_youtube)

        # Aguardar alguns segundos para carregar todo o conteúdo da página
        time.sleep(5)

        # Obter o conteúdo da página
        html_content = driver.page_source

        # Encontrar os links e títulos dos quatro primeiros vídeos encontrados
        soup = BeautifulSoup(html_content, "html.parser")
        videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-video-renderer")
        links = [video.get("href") for video in videos]

        # Imprimir os títulos e links dos quatro primeiros vídeos
        for i in range(4):
            print("Título:", videos[i].get_text().strip())
            print("Link:", "https://www.youtube.com" + links[i], "\n")

        # Fechar o driver
        driver.quit()
        break
    except:
        # Fechar o driver em caso de erro
        driver.quit()
        break

        

