The provided Python scripts generate patterns in all 88 keys of the piano and in all their inversions. Progressions are generated in the combinations of inversions. Patterns are generated in a `patterns/<type>` directory within the current working directory, where `type` is `chords`, `arpeggios`, `scales`, or `progressions`. The usage and currently supported patterns are described below. The Python scripts can easily be modified to support additional patterns. Alternatively, if there is a pattern you would like support for, send me an email and I might add it time permitting and if you ask nicely.

### Generate chords and arpeggios

Chords and arpeggios can be generated using the `generateChords.py` file. The `length`, `offset`, `type`, and `name` must be provided as arguments.

Length: `dyad`, `triad`, or `tetrad`. 

Offset: Offsets are the pitch distances (in semitones) from one note to each subsequent note (the root note is implied). Thus, dyads (2-note chords) require 1 offset, triads (3-note chords) require 2, and tetrads (4-note chords) require 3. For example, for a major chord, the offsets are `4 3`. For a major 7th chord, the offsets are `4 3 4`.

Type: `chord` or `arpeggio`.

Name: A short descriptive name must be provided (e.g., `maj` or `min7b5`)

**Example**: Generate the min7b5 chord in all keys and in all inversions.

``
python generateChords.py tetrad 3 3 4 arpeggio min7b5
``

### Generate scales

Scales can be generated using the `generateScales.py` file. The `offset` and `name` must be provided as arguments.

Offset: The distance from one note to each subsequent note (the root note is implied). For instance, the major/Ionian scale has offsets: `2 2 1 2 2 2`.

Name: A short descriptive name.

**Example**: Generate the Ionian mode in all keys

``
python generateScales.py 2 2 1 2 2 2 ionian
``

### Generate progressions

Progressions can be generated using the `generateProgressions.py` file. Roman numerals (I/i to VII/vii) must be used to specify the chords separated by '-' (dash). Without any extentions/alterations, basic triads are generated. Chords can also be extended or altered by specifying a supported alteration (see table below) separated by a comma between the chord and the alteration. Note that only 3- and 4-chord progressions are currently supported.

Name: A short descriptive name.

**Example** Generate the 2-5-1 progression with the 2 altered by the 7 flat 5 (i.e., min7b5) and the 1 as a major 7, named "ii-V-I".

``
python generateProgressions.py ii,7b5-V-I,maj7 ii-V-I
``

The table below shows the currently supported extensions/alterations.

| Alteration        | Description | 
| ------------- |:-------------:| 
| 7      | Dominant seventh | 
| 7b5      | Seventh flat 5      | 
| 7#5 | Seventh sharp 5      | 
| maj7 | Major seventh |
| maj7b5 | Major seventh flat 5 |
| maj7#5 | Major seventh sharp 5 |

Note: min can be represented using the small Roman numeral.

Chords can be sharpened or flattened using # or b. E.g., II,b. Chords can also be raised/lowered and altered. E.g., II,b,7. A maximum of three arguments are allowed and the chord must be followed by the sharp or flat, and then the alteration.


