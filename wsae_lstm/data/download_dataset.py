import sys
sys.path.append('../')  
import requests

print("Starting raw dataset download...")
url = 'https://ndownloader.figshare.com/files/8493140'
print(f"Raw dataset url: {url}")
myfile = requests.get(url)
open('../../data/raw/raw_data.xlsx', 'wb').write(myfile.content)
# myfile.content.close()
print("Raw dataset download complete. \nCheck data/raw directory for raw_data.xlsx.")