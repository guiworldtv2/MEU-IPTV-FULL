import requests

url = "https://api.github.com/repos/guiworldtv/STR-YT/contents"

try:
    response = requests.get(url)

    if response.status_code == 200:
        if response.headers["Content-Type"] == "application/json":
            contents = response.json()
            m3u_files = [content for content in contents if content["name"].endswith(".m3u")]
            lists = []
            for m3u_file in m3u_files:
                m3u_url = m3u_file["download_url"]
                m3u_response = requests.get(m3u_url)

                if m3u_response.status_code == 200:
                    lists.append((m3u_file["name"], m3u_response.text))
                    
            lists = sorted(lists, key=lambda x: x[0])

            with open("lista.m3u", "w") as f:
                for l in lists:
                    f.write(l[1])
        else:
            print("Error: Invalid content type")
    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error:", e)
