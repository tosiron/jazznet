# jazzNet Dataset
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

The jazzNet dataset is a dataset containing 256GB of audio recordings of 161,840 fundamental piano jazz patterns: chords, arpeggios, scales, and chord progressions, and their inversions. The figure below depicts the taxonomy of the dataset. Details and description of the dataset and labels can be found in the following preprint:

![image](https://user-images.githubusercontent.com/16122125/184457882-e0fe1121-8e34-4d71-bb8e-697a8c81ac15.png)

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
![image](https://user-images.githubusercontent.com/16122125/194719015-a12f6732-7421-4eec-a06d-46fc645415f1.png)

To make the downloads managable, the data are broken down into multiple tarballs if you want to download individual components.

To download everything, use the `download.py` file.

### Metadata
* [All labels](https://tosiron.com/jazznet/dataset/metadata.tar.gz) (2MB)

### MIDI files
* [All patterns](https://tosiron.com/jazznet/dataset/midi.tar.gz) (2.5MB)

### WAV files
All sizes are the compressed data sizes.
* [Chords](https://tosiron.com/jazznet/dataset/wav/chords.tar.gz) (1GB)
* [Arpeggios](https://tosiron.com/jazznet/dataset/wav/arpeggios.tar.gz) (2GB)
* [Scales](https://tosiron.com/jazznet/dataset/wav/scales.tar.gz) (4GB)
* Progressions: Due to the size, the progressions are broken down into 9 downloads featuring the 9 chord progressions.
  * [ii-V-I-maj](https://tosiron.com/jazznet/dataset/wav/progressions/ii-V-I-maj.tar.gz) (6GB)
  * [ii-V-i-min](https://tosiron.com/jazznet/dataset/wav/progressions/ii-V-i-min.tar.gz) (6GB)
  * [ii-triV-I](https://tosiron.com/jazznet/dataset/wav/progressions/ii-triV-I.tar.gz) (6GB) 
  * [I-VI-ii-V-maj](https://tosiron.com/jazznet/dataset/wav/progressions/I-VI-ii-V-maj.tar.gz) (20GB)
  * [i-vi-ii-V-min](https://tosiron.com/jazznet/dataset/wav/progressions/i-vi-ii-V-min.tar.gz) (20GB)
  * [iii-VI-ii-V](https://tosiron.com/jazznet/dataset/wav/progressions/iii-VI-ii-V.tar.gz) (10GB)
  * [I-i#-ii-V](https://tosiron.com/jazznet/dataset/wav/progressions/I-is-ii-V.tar.gz) (20GB)
  * [I-IV7-iii-VI7](https://tosiron.com/jazznet/dataset/wav/progressions/I-IV7-iii-VI7.tar.gz) (20GB)
  * [ii#-V#-ii-V](https://tosiron.com/jazznet/dataset/wav/progressions/iis-Vs-ii-V.tar.gz) (20GB)

### NPZ files (for type and mode prediction using the subsets)
* [Small NPZ files](https://tosiron.com/jazznet/dataset/npz.tar.gz) (8.4GB)
* [Medium NPZ files](https://tosiron.com/jazznet/dataset/npz.tar.gz) (8.4GB)
* [Large NPZ files](https://tosiron.com/jazznet/dataset/npz.tar.gz) (8.4GB)

### Sample uses

### Generate new patterns
You can use the provided Python scripts to generate MIDI files for new patterns and then convert them to WAV files. You will need [MIDI Util](https://pypi.org/project/MIDIUtil/), which can be installed using pip:

```
pip install MIDIUtil
```

You can then generate patterns by specifying the patterns and rules using the `generateChords.py`, `generateScales.py`, and `generateProgressions.py` files. Each file takes in a few arguments to determine the kind of pattern and how to define the patterns. For instance, to generate the major chord in all keys of the standard 88-key piano, you would use the generateChords.py script as follows:

```
python generateChords.py triad 4 3 chord maj
```

where "triad" is the kind of chord and 4 is the distance (in semitones) from the root note; 3 is the distance from the second note, "maj" is the name given to the chord appended to the filenames.

Details can be found in the Generate Patterns folder.

### Citing jazzNet
If you use the jazzNet dataset (or the accompanying paper) in your work, we would appreciate references to the following paper:

##### *jazzNet: An Open-Source Dataset of Fundamental Piano Patterns for Machine Learning Research in Music*, Tosiron Adegbija (2022)

#### BibTeX citation
```
@online{adegbija22,
 author = {Tosiron Adegbija},
 title  = {jazzNet: An Open-Source Dataset of Fundamental Piano Patterns for Machine Learning Research in Music},
 year   = {2022}
}
```

### License
The project is licensed under the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).



