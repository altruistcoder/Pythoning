# Python Chunk Downloader

import requests
from tqdm import tqdm

url = ""  # Add the URL for the file you want to download here.
chunk_s = 512

r = requests.get(url, stream=False)
# stream allows us to download only the request headers till this time without downloading the complete request body

iteration = int(r.headers['content-length'])/chunk_s

with open("python.png", "wb") as f:
    for chunk in tqdm(r.iter_content(chunk_size=chunk_s), total=iteration):
        f.write(chunk)
