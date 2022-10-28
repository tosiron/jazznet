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
    urls = ["https://uweb.engr.arizona.edu/~tosiron/jazznet/arpeggios.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/chords.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/scales.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-small.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz"]

elif sys.argv[1] == "medium":
    urls = ["https://uweb.engr.arizona.edu/~tosiron/jazznet/arpeggios.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/chords.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/scales.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-medium.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz"]

elif sys.argv[1] == "large":
    urls = ["https://uweb.engr.arizona.edu/~tosiron/jazznet/arpeggios.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/chords.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/scales.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-large.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz"]

else:
    urls = ["https://uweb.engr.arizona.edu/~tosiron/jazznet/arpeggios.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/chords.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/scales.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions.tar.gz",
        "https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz"]

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
