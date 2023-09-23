# from-hf-to-torrent
Script to download a HF Model and Upload it to Torrent

## Open Firewall if you are on a Mac

- https://github.com/transmission/transmission/blob/main/docs/Port-Forwarding-Guide.md#open-your-local-firewall

## Available Libraries

- https://github.com/idlesign/torrentool
- https://github.com/rndusr/torf

## Seeding

### 1. Clone the HF Repo

```bash
mkdir data
cd ./data
git lfs install
huggingface-cli lfs-enable-largefiles .
git clone https://huggingface.co/gpt2
```

### 2. Change Parameters

```python
model_name = "gpt2" # name of the cloned folder
absolute_data_path = "/home/filippo/from-hf-to-torrent/data" # absolute path where the data is stored
```

### 3. Create the torrent and seed it

```bash
python main.py
```