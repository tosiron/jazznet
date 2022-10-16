# jazznet Dataset
![image](https://user-images.githubusercontent.com/16122125/184457848-15a2bb14-e5b1-4cef-a7f3-64e93792dd31.png)

<details>
 <summary>Table of contents</summary>
 
 * [Why the dataset was created](#why-the-dataset-was-created)  
 * [How the dataset was created](#how-the-dataset-was-created)
 * [What can you do with the data?](#what-can-you-do-with-the-data)
 * [Download the data](#download-the-data)
 * [Sample uses](#sample-uses)
 * [Citing jazzNet](#citing-jazznet)
 </details>

The jazznet dataset is a dataset containing 256GB of audio recordings of 161,840 fundamental piano jazz patterns: chords, arpeggios, scales, and chord progressions, and their inversions. The figure below depicts the taxonomy of the dataset. 

![image](https://user-images.githubusercontent.com/16122125/196017322-80bc3fdb-ede1-409b-b71b-80860d4d629b.png)

## Why the dataset was created
The dataset is created for machine learning research in music information retrieval (MIR). In general, datasets in the music arena seem to lag datasets in other areas like image recognition. So, this dataset aims to contribute to the body of large-scale datasets available for MIR research.

The general motivation behind the dataset is simple: if you want to learn jazz piano music, you could listen to jazz music and try to replicate it. Or you could learn the fundamentals of jazz piano music (chords, scales, arpeggios, chord progressions) and build on the fundamentals--this would be a more effective way to learn. So, the dataset aims to mimic the data that would be used for effective learning; it contains several automatically generated "fundamental jazz piano patterns". 

The dataset is by no means "complete". For instance, it currently does not contain musical dynamics; it might not contain some of *your* favorite chords or progressions (partly because I probably don't know you and I wasn't trying to please you). But it is extensible. With the provided scripts, you can generate new patterns. Furthermore, if you have a pattern you would like included in the dataset, send me an email, and maybe I will add it. 

## How the dataset was created
There is quite a bit of background music theory for creating the dataset. The theory is summarized in the preprint.

## What can you do with the data?
I imagine it would be a challenging dataset for a variety of ML tasks. You can attempt things like *automatic music transcription*; develop *music recommender systems* based on the kinds of musical patterns a listener likes; *generate new music* based on the patterns in the dataset. And probably a bunch of other interesting things that I'm not thinking about right now. You can also test your image recognition models on spectrograms generated from the music in the dataset.

## Download the data

The table below depicts the statistics of the dataset.  

![image](https://user-images.githubusercontent.com/16122125/196059933-0a3d1331-3049-4621-a00b-4c12905411cf.png)

### Metadata
* [All labels](https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz) (2MB)

### MIDI files
* [All patterns](https://uweb.engr.arizona.edu/~tosiron/jazznet/midi.tar.gz) (2.5MB)

### WAV files

You may use the `download.py` file to download the files. You may specify a subset. For example, to download the `small` subset:

```
python download.py small
```

If no subset is specified, the full dataset is downloaded.

Alternatively, you may manually download the files below. Chords, arpeggios, and scales are part of all subsets. 

* [Chords](https://uweb.engr.arizona.edu/~tosiron/jazznet/chords.tar.gz) (380MB/1GB)
* [Arpeggios](https://uweb.engr.arizona.edu/~tosiron/jazznet/arpeggios.tar.gz) (768MB/1.7GB)
* [Scales](https://uweb.engr.arizona.edu/~tosiron/jazznet/scales.tar.gz) (3.4GB/6.3GB)
* [Progressions](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions.tar.gz) (48.8GB/91.3GB)

Progressions subsets:
* [Progressions-small](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-small.tar.gz) (2GB/3.65GB)
* [Progressions-medium](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-medium.tar.gz) (4.8GBGB/9.1GB)
* [Progressions-large](https://uweb.engr.arizona.edu/~tosiron/jazznet/progressions-large.tar.gz) (12.2GBGB/22.8GB)

### Sample uses

### Generate new patterns
Python scripts are provided to enable you to extend the dataset by generating numerous new patterns. 

Details can be found in the Pattern Generator folder.

### Citing jazznet
If you use the jazznet dataset (or the accompanying paper) in your work, please cite the following paper:

#### BibTeX citation
```
@online{adegbija22,
 author = {Tosiron Adegbija},
 title  = {jazznet: A Dataset of Fundamental Piano Patterns for Music Audio Machine Learning Research},
 year   = {2022}
}
```

### License
The project is licensed under the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).



