This file describes how to generate new patterns using the provided Python scripts.

### Generate chords and arpeggios

Chords and arpeggios can be generated using the `generateChords.py` file. The `length`, `offset`, `type`, and `name` must be provided as arguments.

Length: `dyad`, `triad`, and `tetrad`. 

Offset: Offsets are the distance in semitones from the root note, which is implied. Thus, dyads (2-note chords) require 1 offset, triads (3-note chords) require 2, and tetrads (4-note chords) require 3. For example, for a major chord, the offsets are `4 3`. For a major 7th chord, the offsets are `4 3 4`.

Type: `chord` or `arpeggio`.

Name: A short descriptive name must be provided (e.g., `maj` or `min7b5`)

**Example**: python generateChord.py tetrad 3 3 3 arpeggio min7b5

### Generate scales

### Generate progressions
