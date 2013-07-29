from music21 import *
 
mf.open('Desordem_Pascal.midi')
mf.read()
mf.close()

#len(mf.tracks)

s = midi.translate.midiFileToStream(mf)

s.show('text')


