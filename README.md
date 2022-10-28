# jazznet Dataset
![image](https://user-images.githubusercontent.com/16122125/184457848-15a2bb14-e5b1-4cef-a7f3-64e93792dd31.png)

<details>
 <summary>Table of contents</summary>
 
 * [Why the dataset was created](#why-the-dataset-was-created)  
 * [How the dataset was created](#how-the-dataset-was-created)
 * [What can you do with the data?](#what-can-you-do-with-the-data)
 * [Download the data](download)
 * [Listen to samples](https://tosiron.com/jazznet/)
 * [Generate new patterns](PatternGenerator)
 * [Citing jazzNet](#citing-jazznet)
 * [Contact](#contact)
 </details>

The jazznet dataset is a dataset containing ~95GB of audio recordings of 162520 fundamental piano jazz patterns: chords, arpeggios, scales, and chord progressions, and their inversions in all keys of the 88-key piano. The figure below depicts the taxonomy of the dataset. 

![image](https://user-images.githubusercontent.com/16122125/196017322-80bc3fdb-ede1-409b-b71b-80860d4d629b.png)

The table below depicts the dataset's statistics.  

![image](https://user-images.githubusercontent.com/16122125/197067040-4775a691-6a20-4f31-814d-754ef310f1cd.png)

## Why the dataset was created
The dataset is created for machine learning research in music information retrieval (MIR). In general, datasets in the music arena seem to lag datasets in other areas like image recognition. So, this dataset aims to contribute to the body of large-scale datasets available for MIR research.

The general motivation behind the dataset is simple: if you wanted to learn jazz piano, you could listen to several jazz music pieces and try to replicate them. Or you could learn the fundamentals of jazz piano music (chords, scales, arpeggios, chord progressions) and build on the fundamentals--this would be a more effective way to learn. So, the dataset aims to mimic the data that would be used for effective learning. It contains automatically generated "fundamental jazz piano patterns". 

Another reason (perhaps, the most important reason) why the dataset was created is that I enjoyed doing it. It was very time-consuming to curate the dataset, develop the pattern generator, ascertain correctness of generated patterns and labels, etc. But it was fun and I hope you find it useful.

The dataset is by no means "complete". For instance, it currently does not contain musical dynamics; it might not contain some of *your* favorite chords or progressions (partly because I probably don't know you and I wasn't trying to please you). But it is extensible. With the provided [*pattern generator*](PatternGenerator) scripts, you can generate new patterns. Furthermore, if you have a pattern you would like included in the dataset, [send me an email](#contact), and maybe I will add it if you ask nicely. 

## How the dataset was created
There is a bit of [background music theory](musicBackground.md) necessary for understanding how the dataset was created (although, not necessary for using the dataset). To determine which patterns to include, several resources were surveyed, including jazz piano education books (like The Jazz Piano Book) and numerous jazz standards to identify the basis for the most popular patterns. 

## What can you do with the data?
I imagine it would be an excellent dataset for a variety of challenging ML tasks. The basic tasks include *machine music understanding*, e.g., is some input a chord, scale, or arpeggio. These would be relatively easy for a ML model. More challenging tasks within machine music understanding would be identifying what _kinds_ of patterns are present; e.g., is it an augumented or diminished chord, or what progression is it? Other possible tasks include things like *automatic music transcription* (related to music understanding); develop *music recommender systems* based on the kinds of musical patterns a listener likes (someone who likes a Taylor Swift song might like other songs with only four chords: I, IV, V, VI); *understand and generate music* based on the patterns in the dataset (e.g., learn what arpeggios/scales are played over what chords/progressions). And probably a bunch of other interesting things. You can also test your image recognition models on spectrograms generated from the music in the dataset.

## Download the data

Details on how to download the data can be found [here](download).

### Samples

Listen to a few samples [here.](https://tosiron.com/jazznet/)

### Generate new patterns
Python scripts are provided to enable you to extend the dataset by generating numerous new patterns. 

Details can be found in the [Pattern Generator folder](PatternGenerator).

### Citing jazznet
If you use the jazznet dataset in your work, please cite it as follows:

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



