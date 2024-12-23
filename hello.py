# hello.py
print("Hello, World!")
import requests

repository_link = "https://github.com/Noyalin20020817/hello-python-script"
python_code = '''print("Hello, World!")
import requests

repository_link = "https://github.com/Noyalin20020817/hello-python-script"
python_code = "Your code here"

with open("output.txt", "w") as file:
    file.write(f"GitHub Repository Link: {repository_link}\\n\\n")
    file.write("Python Code:\\n")
    file.write(python_code)

print("output.txt file has been created.")
'''

url = "https://raw.githubusercontent.com/Noyalin20020817/hello-python-script/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    script_content = response.text
    print("Fetched script content:\n", script_content)
else:
    print("Failed to fetch the script. Status code:", response.status_code)

with open("output.txt", "w") as file:
    file.write(f"GitHub Repository Link: {repository_link}\n\n")
    file.write("Python Code:\n")
    file.write(python_code)

print("output.txt file has been created.")
