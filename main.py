import requests

from pathlib import Path
from transmission_rpc import Client
from torf import Torrent

model_name = "gpt2"
absolute_data_path = "/Users/filippopedrazzini/Documents/Work.nosync/from-hf-to-torrent/data/"

BEST_TRACKERS_URL = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"
BEST_TRACKERS = [s for s in requests.get(BEST_TRACKERS_URL).text.split("\n") if s] 

t = Torrent(path=f"./data/{model_name}/", trackers=BEST_TRACKERS, comment=f"{model_name}.")
t.generate()
t.write(f"./torrents/{model_name}.torrent")

c = Client(host="localhost", port=9091)
torrent = c.add_torrent(Path(f"./torrents/{model_name}.torrent"), download_dir=absolute_data_path)
print(f"Added torrent: {torrent.name}")

torrent_info = c.get_torrent(torrent.id)
print(torrent_info.status)