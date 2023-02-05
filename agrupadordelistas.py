import requests

url = "https://api.github.com/repos/guiworldtv/STR-YT/contents"

response = requests.get(url)

if response.status_code == 200:
    contents = response.json()
    m3u_files = [content for content in contents if content["name"].endswith(".m3u")]

    with open("lista1.m3u", "w") as f:
        for m3u_file in m3u_files:
            m3u_url = m3u_file["download_url"]
            m3u_response = requests.get(m3u_url)

            if m3u_response.status_code == 200:
                f.write(m3u_response.text)

else:
    print("Error retrieving contents from GitHub API")
