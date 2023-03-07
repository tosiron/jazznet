# jazznet Dataset [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7192653.svg)](https://doi.org/10.5281/zenodo.7192653)
![image](https://user-images.githubusercontent.com/16122125/184457848-15a2bb14-e5b1-4cef-a7f3-64e93792dd31.png)

The paper describing the jazznet dataset will appear at ICASSP 2023. [Read the preprint](https://arxiv.org/pdf/2302.08632.pdf).

<details>
 <summary>Table of contents</summary>
 
 * [Why the dataset was created](#why-the-dataset-was-created)  
 * [How the dataset was created](#how-the-dataset-was-created)
 * [What can you do with the data?](#what-can-you-do-with-the-data)
 * [Download the data](download)
 * [Listen to samples](https://tosiron.com/jazznet/)
 * [Generate new data](PatternGenerator)
 * [Citing jazznet](#citing-jazznet)
 * [Contact](#contact)
 </details>

The jazznet dataset is an extensible dataset containing 162520 labeled piano patterns: chords, arpeggios, scales, and chord progressions, and their inversions in all keys of the 88-key piano. This results in ~95GB and more than 26K hours of audio. The patterns are guided by the jazz piano genre, but encompass other genres, like country, pop, blues, etc. You can use the dataset as is or easily [generate new data](PatternGenerator) using the provided piano pattern generator.

The figure below depicts the taxonomy of the dataset. 

![image](https://user-images.githubusercontent.com/16122125/196017322-80bc3fdb-ede1-409b-b71b-80860d4d629b.png)

The table below depicts the dataset's statistics.  

![image](https://user-images.githubusercontent.com/16122125/197067040-4775a691-6a20-4f31-814d-754ef310f1cd.png)

## Why the dataset was created
The dataset is created for machine learning research in music information retrieval (MIR). In general, datasets in the music arena seem to lag datasets in other areas like image recognition. So, this dataset aims to contribute to the body of large-scale datasets available for MIR research.

The general motivation behind the dataset is simple: if you wanted to learn jazz piano, you could listen to several jazz music pieces and try to replicate them. Or you could learn the fundamentals of jazz piano music (chords, scales, arpeggios, chord progressions) and build on the fundamentals--this would be a more effective way to learn. So, the dataset aims to mimic the data that would be used for effective learning. It contains automatically generated "fundamental jazz piano patterns". 

Another reason (perhaps, the most important reason) why the dataset was created is that I enjoyed doing it. It was very time-consuming to curate the dataset, develop the pattern generator, ascertain correctness of generated patterns and labels, etc. But it was fun and I hope you find it useful.

The dataset is by no means "complete". For instance, it currently does not contain musical auditory attributes like dynamics and rhythmic variations; it might not contain some of *your* favorite chords or progressions (partly because I probably don't know you and I wasn't trying to please you). But it is extensible. With the provided [*piano pattern generators*](PatternGenerator), you can easily generate tons of new patterns. Furthermore, the scripts are open-source, so you can easily modify them to support even more piano patterns. 

## How the dataset was created
There is a bit of [background music theory](musicBackground.md) necessary for understanding how the dataset was created (although, not necessary for using the dataset). To determine which patterns to include, several resources were surveyed, including jazz piano education books (like The Jazz Piano Book) and numerous jazz standards to identify the basis for the most popular patterns. 

The dataset is automatically generated using what I call _distance-based pattern structures (DBPS)_. DBPS describes the structure of each musical pattern based on the distance between successive pitches within the pattern. This approach enables the data to be automatically [generated](PatternGenerator) in all keys of the piano using symbolic MIDI representation, where the distance between two adjacent pitches is 1 (i.e., a _semitone_). For example, the major triad, with _note0, note1_, and _note2_ can be represented using the structure `[4 3]`, meaning _note1_ is 4 pitches from _note0_, and _note2_ is 3 pitches from _note2_. This holds in all keys of the piano. Similarly, the chords within progressions [can be described](musicBackground.md) using the Roman numerals and generated based on the DBPS approach. 

## What can you do with the data?
I imagine it would be an excellent dataset for a variety of challenging ML tasks. The basic tasks include *machine music understanding*, e.g., is some input a chord, scale, or arpeggio. These would be relatively easy for a ML model. More challenging tasks within machine music understanding would be identifying what _kinds_ of patterns are present; e.g., is it an augumented or diminished chord, or what progression is it? Other possible tasks include things like *automatic music transcription* (related to music understanding); develop *music recommendation systems* based on the kinds of musical patterns a listener likes (someone who likes a Taylor Swift song might like other songs with only four chords: I, IV, V, VI); *understand and generate music* based on the patterns in the dataset (e.g., learn what arpeggios/scales are played over what chords/progressions). And probably a bunch of other interesting things. You can also test your image recognition models on spectrograms generated from the music in the dataset.

## Download the data

Details on how to download the data can be found [here](download). Thanks to the kind people at [Zenodo](https://zenodo.org/) for hosting the dataset!

### Samples

Listen to a few samples [here.](https://tosiron.com/jazznet/)

### Generate new data
Python scripts are provided to enable you to extend the dataset by generating numerous new patterns. 

Details can be found in the [Pattern Generator folder](PatternGenerator).

### Citing jazznet
If you use the jazznet dataset in your work, please cite it as follows:

```
@online{adegbija23_jazznet,
 title  = {jazznet: A Dataset of Fundamental Piano Patterns for Music Audio Machine Learning Research},
 author = {Tosiron Adegbija},
 year   = {2023},
 booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}
 organization = {IEEE}
}
```
### Contact
If you have any questions, comments, or just want to say hi, feel free to email me ([Tosi](https://tosiron.com)): tosiron[at]arizona.edu.

### License
The project is licensed under the [MIT license](LICENSE.md).



