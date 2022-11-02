The dataset is hosted at [Zenodo](https://zenodo.org/deposit/7192653). Download details and direct links are below.

### Metadata
* [All labels](https://zenodo.org/record/7192653/files/metadata.tar.gz?download=1) (2MB)

### MIDI files
* [All patterns](https://zenodo.org/record/7192653/files/midi.tar.gz?download=1) (2.5MB)
  * If the WAV files are too much to download (e.g., due to network bandwidth issues), you could just download the MIDI files and use the [provided script](convertMidiToWav.py) to convert the MIDI files to WAV. You may need to modify the script to include the path to the MIDI files. The script creates WAV directories in the same structure as the MIDI directories. You would need to install Timidity via `pip install timidity`.

### WAV files

There are suggested progression subsets to make the dataset more tractable to download and use. All the chords, arpeggios, and scales are in all the subsets. The table below shows the subset statistics:

| Subset        | Data | 
| ------------- |:-------------:| 
| Small      | 21516 | 
| Medium     | 30328      |
| Large | 52360 |
| Full | 162520 |

You may use the [`download.py`](download.py) file to download the files into the current working directory. You may specify a subset. For example, to download the `small` subset:

```
python download.py small
```

If no subset or anything but `small`, `medium`, or `large` is specified, the full dataset is downloaded.

Alternatively, you may manually download the files below. Chords, arpeggios, and scales are part of all subsets. 

* [Chords](https://zenodo.org/record/7192653/files/chords.tar.gz?download=1) (390MB/1GB)
* [Arpeggios](https://zenodo.org/record/7192653/files/arpeggios.tar.gz?download=1) (787MB/1.7GB)
* [Scales](https://zenodo.org/record/7192653/files/scales.tar.gz?download=1) (3.4GB/6.3GB)
* [Progressions](https://zenodo.org/record/7192653/files/progressions.tar.gz?download=1) (47.4GB/86GB)

Progressions subsets:
* [Progressions-small](https://zenodo.org/record/7192653/files/progressions-small.tar.gz?download=1) (1.9GB/3.4GB)
* [Progressions-medium](https://zenodo.org/record/7192653/files/progressions-medium.tar.gz?download=1) (4.7GB/8.7GB)
* [Progressions-large](https://zenodo.org/record/7192653/files/progressions-large.tar.gz?download=1) (11.8GB/21.4GB)
