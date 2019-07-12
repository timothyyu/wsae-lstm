import sys
sys.path.append('../')  
from os.path import exists
import requests
rdp_part="data/raw/"
rdp = "data/raw/raw_data.xlsx"

print(f"Checking if raw data already downloaded in {rdp_part}...")
print(f"Raw Data already downloaded: {exists(rdp)}")

if exists(rdp) is True:
    print(f"Skipping Raw Data download; dataset already downloaded in {rdp_part}.")
if exists(rdp) is False:
    print("Starting raw dataset download...")
    url = 'https://ndownloader.figshare.com/files/8493140'
    print(f"Raw dataset url: {url}")
    myfile = requests.get(url)
    open('../../data/raw/raw_data.xlsx', 'wb').write(myfile.content)
    print("Raw dataset download complete. \n Check data/raw directory for raw_data.xlsx.")