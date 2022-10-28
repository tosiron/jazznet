#!/usr/bin/env python
#This file generates scales
#USAGE: python generateScales.py <offsets> <name> (the root note is implied)
#E.g., to generate major (Ionian) scales: python generateScales.py 2 2 1 2 2 2 ionian

from midiutil import MIDIFile
import os
import sys
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--offset', required=True, help="Distances of successive pitches")
parser.add_argument('-n', '--name', required=True, help="Short descriptive name, e.g., ionian. No spaces.")

args = parser.parse_args()

noteArray = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
octaveArray = [1, 2, 3, 4, 5, 6, 7, 8]

scaleName = args.name
distances = args.offset
offset = distances.split(" ")

nameArray = []

for o in octaveArray:
	for n in noteArray:
		noteName = n+"-"+str(o)
		nameArray.append(noteName)
		#note = j
#print(nameArray)

for q, j in zip(nameArray, range(24,109)):
    base = j
    noteName = q
    nArray = []
    nArray.append(base)
    note = base

    for i in range(0, len(offset)):
        note = note+int(offset[i])
        nArray.append(note)
	
    for h in range(0,len(nArray)): #range for inversions
        inversion = h
		
        appendInversion = "-"+str(inversion)
        print("\n\n===============GENERATING "+scaleName+" scale. INVERSION: "+str(inversion)+"=================\n\n")
	
        if(inversion==0):
            pass
        else:
            nArray.append(nArray.pop(0)+12)

		#INVERSIONS: 0, 1, 2 MAKE SURE INVERSION IS UPDATED ABOVE!!!
        degrees  = nArray  # MIDI note number; 
        track    = 0
        channel  = 0
        time     = 0    # In beats
        duration = 1    # In beats
        tempo    = 60   # In BPM
        volume   = 100  # 0-127, as per the MIDI standard

        MyMIDI = MIDIFile(1)  # One track
        MyMIDI.addTempo(track, time, tempo)

        for i, pitch in enumerate(degrees):
            MyMIDI.addNote(track, channel, pitch, time+i, duration, volume)
        
        midiName = noteName+'-'+scaleName+appendInversion+".mid"
        filename = "patterns/scales/"+scaleName+"/"+midiName
        path = "patterns/scales/"+scaleName
		
		#create the directory if it doesn't exist
        Path(path).mkdir(parents=True, exist_ok=True)
		
        #os.chdir(path)
        print(path)
        with open(filename, "wb") as output_file:
            MyMIDI.writeFile(output_file)
		#quit()
