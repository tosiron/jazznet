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
