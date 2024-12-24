print("Hello, World!")

repository_link = "https://github.com/Noyalin20020817/hello-python-script"

url = "https://raw.githubusercontent.com/Noyalin20020817/hello-python-script/main/hello.py"

# Fetch the script content from the URL
import requests
response = requests.get(url)

if response.status_code == 200:
    script_content = response.text
    print("Fetched script content:\n", script_content)
else:
    print("Failed to fetch the script. Status code:", response.status_code)
