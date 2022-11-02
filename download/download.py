#download the jazznet dataset
#You may specify "small", "medium", or "large". No arguments downloads the full dataset.

import requests
import time
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
import os
import sys
from pathlib import Path

if sys.argv[1] == "small":
    urls = ["https://zenodo.org/record/7192653/files/arpeggios.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/chords.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/scales.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/progressions-small.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/metadata.tar.gz?download=1"]

elif sys.argv[1] == "medium":
    urls = ["https://zenodo.org/record/7192653/files/arpeggios.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/chords.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/scales.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/progressions-medium.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/metadata.tar.gz?download=1"]

elif sys.argv[1] == "large":
    urls = ["https://zenodo.org/record/7192653/files/arpeggios.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/chords.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/scales.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/progressions-large.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/metadata.tar.gz?download=1"]

else:
    urls = ["https://zenodo.org/record/7192653/files/arpeggios.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/chords.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/scales.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/progressions.tar.gz?download=1",
        "https://zenodo.org/record/7192653/files/metadata.tar.gz?download=1"]

def urlsToDownload(url):
    try:
        path = "wav"
        Path(path).mkdir(parents=True, exist_ok=True)
        file_name_1 = url.split("/")
        file_name = file_name_1[-1]
        print("Downloading: ", file_name)
        r = requests.get(url)
        with open(file_name, 'wb') as f:
            f.write(r.content)
        return url
    except:
        print("Something went wrong and the files couldn't be downloaded. You may need to download them manually.")

#parallel download
def parallelDownload(url):
    cpus = cpu_count()
    results = ThreadPool(cpus - 1).imap_unordered(urlsToDownload, url)

parallelDownload(urls)
