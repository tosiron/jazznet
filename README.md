# jazzNet Dataset
The jazzNet dataset is a dataset containing 256GB of audio recordings of 161,840 fundamental piano jazz patterns: chords, arpeggios, scales, and chord progressions, and their inversions. The figure below depicts the taxonomy of the dataset. 
![image](https://user-images.githubusercontent.com/16122125/171737773-beefb793-0653-4d30-8c7b-179db3eb73b3.png)

## Data

The table below depicts the statistics of the dataset.  
![image](https://user-images.githubusercontent.com/16122125/171740900-dcdb079c-5d48-4f2e-84de-f6aecb5e16a5.png)

To make the downloads tractable, the data are broken down into multiple tarballs and NPZ subsets.

### WAV files
All sizes are the compressed data sizes.
* [Chords](https://tosiron.com/jazznet/dataset/wav/chords.tar.gz) (1GB)
* [Arpeggios](https://tosiron.com/jazznet/dataset/wav/arpeggios.tar.gz) (2GB)
* [Scales](https://tosiron.com/jazznet/dataset/wav/scales.tar.gz) (4GB)
* Progressions: Due to the size, the progressions are broken down into 9 downloads featuring the 9 chord progressions.
  * I-i#-ii-V (20GB)
  * ii#-V#-ii-V (20GB)
  * iii-IV-ii-V (10GB)
  * ii-IV-I-maj (6GB)
  * ii-IV-i-min (6GB)
  * ii-triV-I (6GB)
  * I-IV7-iii-VI7 (20GB)
  * I-VI-ii-V-maj (20GB)
  * i-vi-ii-V-min (20GB)

### MIDI files
* All patterns

### Metadata
* All labels
* Large subset
* Medium Subset
* Small subset
* Subsets Info

### NPZ files (for type and mode prediction using the subsets)
The NPZ arrays contain the mel-spectogram features.
* Type small
* Type medium
* Type large
* Mode small
* Mode medium
* Mode large
