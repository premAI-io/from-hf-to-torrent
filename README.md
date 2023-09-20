# from-hf-to-torrent
Script to download a HF Model and Upload it to Torrent

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