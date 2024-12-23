# hello-python-scr# hello.py
print("Hello, World!")
import requests

# Replace with your GitHub raw file URL
url = "https://raw.githubusercontent.com/yourusername/my-python-scripts/main/hello.py"

response = requests.get(url)

if response.status_code == 200:
    with open('hello_from_github.py', 'w') as f:
        f.write(response.text)
    print("File downloaded successfully!") 
else:
    print("Failed to fetch the file.")
  
