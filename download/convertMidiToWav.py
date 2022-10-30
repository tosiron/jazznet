#!/usr/bin/env python

import os, glob
import subprocess
from pathlib import Path

midi_dir = "patterns" #directory containing the generated MIDI files

wav_dir = "wav" #directory where the converted WAV files are stored

for dir1 in os.listdir(midi_dir):
	midi1 = os.path.join(midi_dir, dir1)
	wav1 = os.path.join(wav_dir,dir1)

	for dir2 in os.listdir(midi1):
		midi_path = os.path.join(midi1, dir2)
		wav_store = os.path.join(wav1, dir2)
		
		#create the wav directory if it doesn't already exist
		isExist = os.path.exists(wav_store)
		if not isExist:
			os.makedirs(wav_store)
		
		os.chdir(midi_path)
		for file in glob.glob("*.mid"):
			newname = Path(file).stem #remove .mid extension
			
			#run timidity; input is the midi file, output is the wav file in the equivalent directory
			subprocess.call(['timidity', midi_path+'/'+file, '-Ow1', '-s', '16kHz', '-o', wav_store+'/'+newname+'.wav'])

	#		

