#!/usr/bin/env python

from multiprocessing.sharedctypes import Value
from xml.dom import ValidationErr
from midiutil import MIDIFile
import os
import sys
from pathlib import Path

style = "progressions" #chords, arpeggios, scales
#chords, arpeggios

noteArray = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
octaveArray = [1, 2, 3, 4, 5, 6, 7, 8]

alterationsArr = ["7", "7b5", "7#5", "maj7", "maj7b5", "maj7#5"]
#check arguments
if len(sys.argv) < 3:
	raise ValueError("Too few arguments are provided. You must specify the progression to generate.\nThe format is: generateProgressions.py <progression> <name>")
elif len(sys.argv) > 3:
	raise ValueError("Too many arguments are provided.")

progChords = sys.argv[1].split('-')

if((len(progChords) != 3) and (len(progChords) != 4)):
	raise ValueError("Only 3- and 4-chord progressions are currently supported.")
progressionName = sys.argv[-1]

inversion = 0

nameArray = []

for o in octaveArray:
	for n in noteArray:
		noteName = n+'-'+str(o)
		nameArray.append(noteName)
		#note = j
#print(nameArray)

def baseChords(firstNote, numeral):
	if numeral.isupper():
		note1 = firstNote
		note2 = note1+4
		note3 = note2+3
	elif numeral.islower():
		note1 = firstNote
		note2 = note1+3
		note3 = note2+4
	return note1, note2, note3

def raiseNote(note1, note2, note3, raiseVal):
	if raiseVal == "#":
		note1 = note1+1
		note2 = note2+1
		note3 = note3+1
	elif raiseVal == "b":
		note1 = note1-1
		note2 = note2-1
		note3 = note3-1
	return note1, note2, note3

def chordAlteration(note1, note2, note3, ext):
	if ext == "7":
		note4 = note3+3
	elif ext == "7b5":
		note3 = note3-1
		note4 = note3+4
	elif ext == "7#5":
		note3 = note3+1
		note4 = note3+4
	elif ext == "maj7":
		note4 = note3+4
	elif ext == "maj7b5":
		note3 = note3-1
		note4 = note3+4
	elif ext == "maj7#5":
		note3 = note3+1
		note4 = note3+4
	return note1, note2, note3, note4

def chordInversions3(note1, note2, note3, inv):
	if inv == 1:
		note1 = note1+12
	elif inv == 2:
		note1 = note1+12
		note2 = note2+12 
	return note1, note2, note3 

def chordInversions4(note1, note2, note3, note4, inv):
	if inv == 1:
		note1 = note1+12
	elif inv == 2:
		note1 = note1+12
		note2 = note2+12
	elif inv == 3:
		note1 = note1+12
		note2 = note2+12
		note3 = note3+12
	return note1, note2, note3, note4

for q, j in zip(nameArray, range(24,109)):
	#print(q+"="+str(j));
	base = j
	noteName = q
	
	chord = []
	chordArr = []

	for numeral in progChords:
		numeralArr = numeral.split(',')
		if numeralArr[0] in ["I", "i"]:
			firstNote = base
		elif numeralArr[0] in ["II", "ii"]:
			firstNote = base+2
		elif numeralArr[0] in ["III", "iii"]:
			firstNote = base+4
		elif numeralArr[0] in ["IV", "iv"]:
			firstNote = base+5
		elif numeralArr[0] in ["V", "v"]:
			firstNote = base+7
		elif numeralArr[0] in ["VI", "vi"]:
			firstNote = base+9
		elif numeralArr[0] in ["VII", "vii"]:
			firstNote = base+11
		else:
			raise ValueError("One of the chords is unrecognized. Accepted chords are I/i - VII/vii")
		
		#define base chord
		note1, note2, note3 = baseChords(firstNote, numeralArr[0])
		chord = note1, note2, note3 

		if len(numeralArr) > 1:
			if numeralArr[1] not in ["#", "b"] and numeralArr[1] not in alterationsArr:
				raise ValueError("An unrecognized character has been provided. The comma must be followed by # or b or by a supported alteration.")
			else:
				if(numeralArr[1] in ["#", "b"]): 
					note1, note2, note3 = raiseNote(note1, note2, note3, numeralArr[1])
				elif(numeralArr[1] in alterationsArr): #there's an alteration
					note1, note2, note3, note4 = chordAlteration(note1, note2, note3, numeralArr[1])
					chord = note1, note2, note3, note4
		if len(numeralArr) == 3: #there's an alteration
			if numeralArr[1] in alterationsArr:
				raise ValueError("If two changes are provided, the first must be a # or b, and the second must be an alteration (e.g., ii,#,7).")
			elif numeralArr[2] in alterationsArr: #first check that the alteration is valid
				note1, note2, note3, note4 = chordAlteration(note1, note2, note3, numeralArr[2])
				chord = note1, note2, note3, note4
			else:
				raise ValueError("An unrecognized alteration has been provided.")
		elif len(numeralArr) > 3:
			raise ValueError("More arguments than accepted have been provided. Only provide the chord and the alteration separated by a comma. E.g.: ii,min7")
		
		chordArr.append(chord)
	
	track    = 0
	channel  = 0
	time     = 0    # In beats
	duration = 2    # In beats
	tempo    = 60   # In BPM
	volume   = 100  # 0-127, as per the MIDI standard

	if len(chordArr) == 3:
		num = 0
		tempArr1 = chordArr[0]
		tempArr2 = chordArr[1]
		tempArr3 = chordArr[2]
		
		for c1 in range(0, len(tempArr1)):
			print("\n\n===============GENERATING "+progressionName+" "+style+". KEY: "+noteName+"=================\n\n")
			for c2 in range(0, len(tempArr2)):
				for c3 in range(0, len(tempArr3)):
					tempArr1 = chordArr[0]
					tempArr2 = chordArr[1]
					tempArr3 = chordArr[2]
					if len(tempArr1) == 3:
						tempArr1 = chordInversions3(tempArr1[0], tempArr1[1], tempArr1[2], c1)
					else:
						tempArr1 = chordInversions4(tempArr1[0], tempArr1[1], tempArr1[2], tempArr1[3], c1)
					
					if len(tempArr2) == 3:
						tempArr2 = chordInversions3(tempArr2[0], tempArr2[1], tempArr2[2], c2)
					else:
						tempArr2 = chordInversions4(tempArr2[0], tempArr2[1], tempArr2[2], tempArr2[3], c2)
					
					if len(tempArr3) == 3:
						tempArr3 = chordInversions3(tempArr3[0], tempArr3[1], tempArr3[2], c3)
					else:
						tempArr3 = chordInversions4(tempArr3[0], tempArr3[1], tempArr3[2], tempArr3[3], c3)
					tempArr = tempArr1, tempArr2, tempArr3
					#print(chordArr)
					
					MyMIDI = MIDIFile(1)  # One track
					MyMIDI.addTempo(track, time, tempo)
					timeOffset = 0
					for c in tempArr:
						#print(c)
						chordNotes = c

						for cn in chordNotes:
							MyMIDI.addNote(track, channel, cn, time+timeOffset, duration, volume)	
						timeOffset = timeOffset + 2			
					
					midiName = noteName+"-"+progressionName+'-'+str(num)+".mid"
					filename = "patterns/"+style+"/"+progressionName+"/"+midiName
					#print(filename)
					path = "patterns/"+style+"/"+progressionName
					
					Path(path).mkdir(parents=True, exist_ok=True)
					
					with open(filename, "wb") as output_file:
						MyMIDI.writeFile(output_file)
					inversion = inversion+1
					num=num+1

	elif len(chordArr) == 4:
		num = 0
		tempArr1 = chordArr[0]
		tempArr2 = chordArr[1]
		tempArr3 = chordArr[2]
		tempArr4 = chordArr[3]

		for c1 in range(0, len(tempArr1)):
			print("\n\n===============GENERATING "+progressionName+" "+style+". KEY: "+noteName+"=================\n\n")
			for c2 in range(0, len(tempArr2)):
				for c3 in range(0, len(tempArr3)):
					for c4 in range(0, len(tempArr4)):
						tempArr1 = chordArr[0]
						tempArr2 = chordArr[1]
						tempArr3 = chordArr[2]
						tempArr4 = chordArr[3]
						if len(tempArr1) == 3:
							tempArr1 = chordInversions3(tempArr1[0], tempArr1[1], tempArr1[2], c1)
						else:
							tempArr1 = chordInversions4(tempArr1[0], tempArr1[1], tempArr1[2], tempArr1[3], c1)

						if len(tempArr2) == 3:
							tempArr2 = chordInversions3(tempArr2[0], tempArr2[1], tempArr2[2], c2)
						else:
							tempArr2 = chordInversions4(tempArr2[0], tempArr2[1], tempArr2[2], tempArr2[3], c2)
						
						if len(tempArr3) == 3:
							tempArr3 = chordInversions3(tempArr3[0], tempArr3[1], tempArr3[2], c3)
						else:
							tempArr3 = chordInversions4(tempArr3[0], tempArr3[1], tempArr3[2], tempArr3[3], c3)
						
						if len(tempArr4) == 3:
							tempArr4 = chordInversions3(tempArr4[0], tempArr4[1], tempArr4[2], c4)
						else:
							tempArr4 = chordInversions4(tempArr4[0], tempArr4[1], tempArr4[2], tempArr4[3], c4)
						tempArr = tempArr1, tempArr2, tempArr3, tempArr4
						
						MyMIDI = MIDIFile(1)  # One track
						MyMIDI.addTempo(track, time, tempo)
						timeOffset = 0
						for c in tempArr:
							#print(c)
							chordNotes = c
							
							for cn in chordNotes:
								MyMIDI.addNote(track, channel, cn, time+timeOffset, duration, volume)	
							timeOffset = timeOffset + 2			
						
						midiName = noteName+"-"+progressionName+'-'+str(num)+".mid"
						filename = "patterns/"+style+"/"+progressionName+"/"+midiName
						#print(filename)
						path = "patterns/"+style+"/"+progressionName
						
						Path(path).mkdir(parents=True, exist_ok=True)
						
						with open(filename, "wb") as output_file:
							MyMIDI.writeFile(output_file)
						inversion = inversion+1
						num = num+1
	

