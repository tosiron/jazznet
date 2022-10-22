The table below depicts the dataset's statistics.  

![image](https://user-images.githubusercontent.com/16122125/197067040-4775a691-6a20-4f31-814d-754ef310f1cd.png)

### [Metadata](metadata)
* [All labels](https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz) (2MB)

### MIDI files
* [All patterns](https://uweb.engr.arizona.edu/~tosiron/jazznet/midi.tar.gz) (2.5MB)

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

* [Chords](https://uweb.engr.arizona.edu/~tosiron/jazznet/chords.tar.gz) (380MB/1GB)
* [Arpeggios](https://uweb.engr.arizona.edu/~tosiron/jazznet/arpeggios.tar.gz) (768MB/1.7GB)
* [Scales](https://uweb.engr.arizona.edu/~tosiron/jazznet/scales.tar.gz) (3.4GB/6.3GB)
* [Progressions](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions.tar.gz) (48.8GB/91.3GB)

Progressions subsets:
* [Progressions-small](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-small.tar.gz) (1.9GB/3.4GB)
* [Progressions-medium](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-medium.tar.gz) (4.6GBGB/8.7GB)
* [Progressions-large](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-large.tar.gz) (11.6GB/21.4GB)
