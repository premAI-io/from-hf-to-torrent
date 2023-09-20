import os
import requests

from pathlib import Path
from transmission_rpc import Client
from torf import Torrent

BEST_TRACKERS_URL = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"
BEST_TRACKERS = [s for s in requests.get(BEST_TRACKERS_URL).text.split("\n") if s] 

models = [
    "CodeLlama-34b-Instruct-hf",
    "StableBeluga2",
    "falcon-180B-chat"
]
data_path = "./data/"
absolute_data_path = os.path.abspath(data_path)
print(f"Absolute data path: {absolute_data_path}")

c = Client(host="localhost", port=9091)

torrents = c.get_torrents()
torrent_names = [t.name for t in torrents]

for model in models:
    if model not in torrent_names:
        t = Torrent(path=f"./data/{model}/", trackers=BEST_TRACKERS, comment=f"{model}.")
        t.generate()
        t.write(f"./torrents/{model}.torrent")
        print(f"Magnet URL: {t.magnet()}")

        torrent = c.add_torrent(Path(f"./torrents/{model}.torrent"), download_dir=absolute_data_path)
        print(f"Added torrent: {torrent.name}")

        torrent_info = c.get_torrent(torrent.id)
        print(torrent_info.status)