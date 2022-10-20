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
 * [Contact](#contact)
 </details>

The jazznet dataset is a dataset containing ~100GB of audio recordings of 162520 fundamental piano jazz patterns: chords, arpeggios, scales, and chord progressions, and their inversions in all keys of the 88-key piano. The figure below depicts the taxonomy of the dataset. 

![image](https://user-images.githubusercontent.com/16122125/196017322-80bc3fdb-ede1-409b-b71b-80860d4d629b.png)

## Why the dataset was created
The dataset is created for machine learning research in music information retrieval (MIR). In general, datasets in the music arena seem to lag datasets in other areas like image recognition. So, this dataset aims to contribute to the body of large-scale datasets available for MIR research.

The general motivation behind the dataset is simple: if you wanted to learn jazz piano, you could listen to several jazz music pieces and try to replicate them. Or you could learn the fundamentals of jazz piano music (chords, scales, arpeggios, chord progressions) and build on the fundamentals--this would be a more effective way to learn. So, the dataset aims to mimic the data that would be used for effective learning. It contains automatically generated "fundamental jazz piano patterns". 

Another reason why the dataset was created is that I enjoyed doing it. It was very time-consuming to curate the dataset, write the generation scripts, ascertain correctness of generated patterns and labels, etc. But it was fun.

The dataset is by no means "complete". For instance, it currently does not contain musical dynamics; it might not contain some of *your* favorite chords or progressions (partly because I probably don't know you and I wasn't trying to please you). But it is extensible. With the provided *pattern generator* scripts, you can generate new patterns. Furthermore, if you have a pattern you would like included in the dataset, [send me an email](#contact), and maybe I will add it if you ask nicely. 

## How the dataset was created
There is a bit of [background music theory](musicBackground.md) necessary for understanding how the dataset was created (although, not necessary for using the dataset). To determine which patterns to include, several resources were surveyed, including jazz piano education books (like The Jazz Piano Book) and numerous jazz standards to identify the basis for the most popular patterns. 

## What can you do with the data?
I imagine it would be a good dataset for a variety of challenging ML tasks. You can attempt things like *automatic music transcription*; develop *music recommender systems* based on the kinds of musical patterns a listener likes; *understand and generate music* based on the patterns in the dataset. And probably a bunch of other interesting things. You can also test your image recognition models on spectrograms generated from the music in the dataset.

## Download the data

The table below depicts the dataset's statistics.  

![image](https://user-images.githubusercontent.com/16122125/197067040-4775a691-6a20-4f31-814d-754ef310f1cd.png)

### Metadata
* [All labels](https://uweb.engr.arizona.edu/~tosiron/jazznet/metadata.tar.gz) (2MB)

### MIDI files
* [All patterns](https://uweb.engr.arizona.edu/~tosiron/jazznet/midi.tar.gz) (2.5MB)

### WAV files

You may use the [`download.py`](download.py) file to download the files. You may specify a subset. For example, to download the `small` subset:

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

### Samples

Some samples can be found [here.](https://tosiron.com/jazznet/) 

### Generate new patterns
Python scripts are provided to enable you to extend the dataset by generating numerous new patterns. 

Details can be found in the [Pattern Generator folder](Pattern%20Generator).

### Citing jazznet
If you use the jazznet dataset (or the accompanying paper) in your work, please cite the following paper:

```
@online{adegbija22,
 author = {Tosiron Adegbija},
 title  = {jazznet: A Dataset of Fundamental Piano Patterns for Music Audio Machine Learning Research},
 year   = {2022}
}
```
### Contact
If you have any questions, comments, or just want to say hi, feel free to email me (Tosi): tosiron[at]arizona.edu.

### License
The project is licensed under the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).



