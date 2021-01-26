from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

root_url = "https://scifi.media/wp-content/uploads/t/x/"

def get_script(ep):
    script_url = f"{root_url}{ep}.txt"
    request_body = requests.get(script_url).text
    bs = BeautifulSoup(request_body, 'html.parser')
    text = bs.get_text()
    return text

def save_scripts(start, end, filename):
    sum = end + 1
    with open(filename, 'w') as f:
        for i in range(start, sum):
            script = get_script(i)
            f.write(f"{script}")

# scrapes and saves x-files script text for episodes 1 to 101 (there are 209 total)
save_scripts(1, 100, 'xfiles_101.txt')
