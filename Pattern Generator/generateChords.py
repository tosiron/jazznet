#!/usr/bin/env python
#This file generates chords and arpeggios
#USAGE: python generateScales.py <chordLength> <offsets> <name> (the root note is implied)
#E.g., to generate min7b5 chord: python generateScales.py tetrad 3 3 3 chord min7b5

from midiutil import MIDIFile
import os
import sys
from pathlib import Path

noteArray = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
octaveArray = [1, 2, 3, 4, 5, 6, 7, 8]

chordLength = sys.argv[1]
if chordLength not in ["dyad", "triad", "tetrad"]:
	raise ValueError("The chord type is not recognized. Options are dyad, triad, and tetrad.")

if chordLength == "dyad":
	offset1 = int(sys.argv[2])
	style = sys.argv[3]
	chordType = sys.argv[4]
elif chordLength == "triad":
	offset1 = int(sys.argv[2])
	offset2 = int(sys.argv[3])
	style = sys.argv[4]
	chordType = sys.argv[5]
elif chordLength == "tetrad":
	offset1 = int(sys.argv[2])
	offset2 = int(sys.argv[3])
	offset3 = int(sys.argv[4])
	style = sys.argv[5]
	chordType = sys.argv[6]

if style not in ["arpeggio", "chord"]:
	raise ValueError("The only options for style are arpeggio and chord")

nameArray = []

for o in octaveArray:
	for n in noteArray:
		noteName = n+"-"+str(o)
		nameArray.append(noteName)
		#note = j
#print(nameArray)

def createDyad(inversion, base, offset1):
	if(inversion==0):
		note1 = base
		note2 = base+offset1

	elif(inversion==1):
		note1 = base+offset1
		note2 = base+12
	return note1, note2

def createTriad(inversion, base, offset1, offset2):
	if(inversion==0):
		note1 = base
		note2 = base+offset1
		note3 = note2+offset2

	elif(inversion==1):
		note1 = base+offset1
		note2 = note1+offset2
		note3 = base+12

	elif(inversion==2):
		note1 = base+offset1+offset2
		note2 = base+12
		note3 = note2+offset1
	
	return note1, note2, note3

def createTetrad(inversion, base, offset1, offset2, offset3):
	if(inversion==0):
		note1 = base
		note2 = note1+offset1
		note3 = note2+offset2
		note4 = note3+offset3

	elif(inversion==1):
		note1 = base+offset1
		note2 = note1+offset2
		note3 = note2+offset3
		note4 = base+12

	elif(inversion==2):
		note1 = base+offset1+offset2
		note2 = note1+offset3
		note3 = base+12
		note4 = note3+offset1
	
	elif(inversion==3):
		note1 = base+offset1+offset2+offset3
		note2 = base+12
		note3 = note2+offset1
		note4 = note3+offset2

	return note1, note2, note3, note4 

for q, j in zip(nameArray, range(24,109)):
	#print(q+"="+str(j));
	base = j
	noteName = q

	if chordLength == "dyad":
		upperRange = 2
	elif chordLength == "triad":
		upperRange = 3
	elif chordLength == "tetrad":
		upperRange = 4
	
	for h in range(0,upperRange): #range for inversions
		inversion = h
		
		appendInversion = "-"+str(inversion)
		print("\n\n===============GENERATING "+chordType+" "+style+". INVERSION: "+str(inversion)+"=================\n\n")
	
		if chordLength == "dyad":
			note1, note2 = createDyad(inversion, base, offset1)
			degrees = [note1, note2]
		elif chordLength == "triad":
			note1, note2, note3 = createTriad(inversion, base, offset1, offset2)
			degrees = [note1, note2, note3]
		elif chordLength == "tetrad":
			note1, note2, note3, note4 = createTetrad(inversion, base, offset1, offset2, offset3)
			degrees = [note1, note2, note3, note4]

		#INVERSIONS: 0, 1, 2 MAKE SURE INVERSION IS UPDATED ABOVE!!!
		#degrees  = [note1,note2]  # MIDI note number; 
		track    = 0
		channel  = 0
		time     = 0    # In beats
		duration = 1    # In beats
		tempo    = 60   # In BPM
		volume   = 100  # 0-127, as per the MIDI standard

		MyMIDI = MIDIFile(1)  # One track
		MyMIDI.addTempo(track, time, tempo)

		if style == "arpeggio":
			for i, pitch in enumerate(degrees):
				MyMIDI.addNote(track, channel, pitch, time+i, duration, volume) #time + i for arpeggios
		elif style == "chord":
			for i, pitch in enumerate(degrees):
				MyMIDI.addNote(track, channel, pitch, time, duration, volume) #time + i for arpeggios
		
		midiName = noteName+'-'+chordType+'-'+style+appendInversion+".mid"
		filename = "patterns/"+style+"/"+chordType+"/"+midiName
		print(filename)
		path = "patterns/"+style+"/"+chordType
		
		#create the directory if it doesn't exist
		Path(path).mkdir(parents=True, exist_ok=True)
		
		print(path)
		with open(filename, "wb") as output_file:
			MyMIDI.writeFile(output_file)
		#quit()

