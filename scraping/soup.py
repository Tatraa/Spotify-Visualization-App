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
            tracks_recorded = cells[4].text.replace("<td style="">","").replace("</td>","")
            songs_over_1B = cells[5].text.replace("<td style="">","").replace("</td>","")
            songs_over_100m = cells[6].text.replace("<td style="">","").replace("</td>","")
            songs_over_10m = cells[7].text.replace("<td style="">","").replace("</td>","")
            songs_over_1m = cells[8].text.replace("<td style="">","").replace("</td>","")

            print("Artist:", artist)
            print("Lead Streams:", lead_streams)
            print("Feat Streams:", feat_streams)
            print(tracks_recorded)
            print(songs_over_1B)
            print(songs_over_10m)
            print(songs_over_1m)
            print(songs_over_100m)

            artist_data = [artist, lead_streams, feat_streams, tracks_recorded,
                           songs_over_1m, songs_over_10m, songs_over_100m, songs_over_1B]
            artists_data.append(artist_data)

        artist_csv = "artists_data.csv"
        with open(artist_csv, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["artist", "lead Streams", "feat Streams", "tracks recorded",
                             "songs over 1m","songs over 10m", "songs over 100m", "songs over 1B"])

            writer.writerows(artists_data)

        print(f"Data has been saved to {artist_csv}")

    else:
        print("Data can not be extracted:", response.status_code)

artist_data_import()
