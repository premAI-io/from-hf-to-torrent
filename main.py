import os
import requests
from pathlib import Path
from tqdm import tqdm
from functools import partial
from transmission_rpc import Client
from torf import Torrent

BEST_TRACKERS_URL = (
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
)
BEST_TRACKERS = [s for s in requests.get(BEST_TRACKERS_URL).text.split("\n") if s]

models = ["CodeLlama-34b-Instruct-hf", "StableBeluga2"]  #TODO: , "falcon-180B-chat"]
data_path = "./data/"
torrents_dir = "./torrents/"


def upload_progress(*args, pbar):
    pbar.update(1)


def create_torrent(
    model_name,
    trackers=BEST_TRACKERS,
    file_path=data_path,
    torrent_dir=torrents_dir,
    comment=None,
):
    if not os.path.exists(data_path + model_name):
        print(f"Model '{model_name}' data directory does not exist.")
        return
    print(f"Starting {model_name} torrent creation...")
    t = Torrent(
        path=file_path + model_name,
        trackers=trackers,
        comment=comment or f"{model_name}.",
        webseeds=["http://128.140.126.131:8989/"],
    )
    pbar = tqdm(total=t.pieces)
    t.generate(callback=partial(upload_progress, pbar=pbar))
    pbar.close()
    t.write(torrent_dir + f"{model_name}.torrent")
    print(f"Magnet URL for '{model_name}': {t.magnet()}")


def seed_torrent(model_name):
    c = Client(host="localhost", port=9091)
    torrents = c.get_torrents()
    torrent_names = [t.name for t in torrents]

    if model_name not in torrent_names:
        torrent = c.add_torrent(
            Path(torrents_dir + f"{model_name}.torrent"), download_dir="/downloads"
        )
        print(f"Added torrent '{model_name}': {torrent.name}")

        torrent_info = c.get_torrent(torrent.id)
        print(torrent_info.status)


def main():
    for model in models:
        create_torrent(model)
        seed_torrent(model)


if __name__ == "__main__":
    main()
