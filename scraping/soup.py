import json
import re
import pandas as pd
import urllib
from urllib.request import Request
import csv
import requests
from bs4 import BeautifulSoup

url = "https://chartmasters.org/most-streamed-artists-ever-on-spotify/"

response = requests.get(url)
def artist_data_import():
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")

        table = soup.find("table")

        # find all rows in table
        rows = table.find_all("tr")

        artists_data = []
        for row in rows[1:]:
            # find all the 'td's
            cells = row.find_all("td")

            # artist info
            artist_raw = cells[2].text.strip()
            artist = re.sub(r"\d+ day\(s\) old data", "", artist_raw).strip()
            lead_streams = int(cells[3].text.replace(",","").strip())
            feat_streams = int(cells[9].text.replace(",","").strip())

            print("Artist:", artist)
            print("Lead Streams:", lead_streams)
            print("Feat Streams:", feat_streams)
            print()

            artist_data = [artist, lead_streams, feat_streams]
            artists_data.append(artist_data)

        artist_csv = "artists_data.csv"
        with open(artist_csv, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["artist", "lead Streams", "feat Streams"])

            writer.writerows(artists_data)

        print(f"Data has been saved to {artist_csv}")

    else:
        print("Data can not be extracted:", response.status_code)

artist_data_import()