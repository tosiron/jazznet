The provided Python scripts generate patterns in all their inversions and in all 88 keys of the piano.

### Generate chords and arpeggios

Chords and arpeggios can be generated using the `generateChords.py` file. The `length`, `offset`, `type`, and `name` must be provided as arguments.

Length: `dyad`, `triad`, and `tetrad`. 

Offset: Offsets are the distance in semitones from one note to each subsequent note (the root note is implied). Thus, dyads (2-note chords) require 1 offset, triads (3-note chords) require 2, and tetrads (4-note chords) require 3. For example, for a major chord, the offsets are `4 3`. For a major 7th chord, the offsets are `4 3 4`.

Type: `chord` or `arpeggio`.

Name: A short descriptive name must be provided (e.g., `maj` or `min7b5`)

**Example**: Generate the min7b5 chord in all keys

``
python generateChord.py tetrad 3 3 3 arpeggio min7b5
``

### Generate scales

Scales can be generated using the `generateScales.py` file. The `offset` and `name` must be provided as arguments.

Offset: The distance from one note to each subsequent note (the root note is implied). For instance, the major/Ionian scale has offsets: `2 2 1 2 2 2`.

Name: A short descriptive name.

**Example**: Generate the Ionian mode in all keys

``
python generateChord.py 2 2 1 2 2 2 ionian
``

### Generate progressions

Progressions can be generated using the `generateProgressions.py` file. Roman numerals (I/i to VII/vii) must be used to specify the chords separated by '-' (dash). Without any alterations, basic triads are generated. Chords can also be altered by specifying a supported alteration (see table below) separated by a comma between the chord and the alteration. 

**Example** Generate the 2-5-1 progression with the 2 altered by the 7 flat 5 (i.e., min7b5) and the 1 as a major 7

``
python generateProgression.py ii,7b5-V-I,maj7
``

Current supported alterations are: "7" (seventh); "maj7"; "7b5" (seventh flat 5; usually used with minor chords)
