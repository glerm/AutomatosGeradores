from music21 import *

mf = midi.MidiFile() 
mf.open('Desordem_Pascal.midi')
mf.read()
mf.close()

#len(mf.tracks)

s = midi.translate.midiFileToStream(mf)

#formato music21
#s.show('text')

#grid matrix
#graph.plotStream(s)

#frequencia de pitches - histograma
graph.plotStream(s, 'PlotHistogramPitchClass')

#pitches e suas duracoes
#s.plot(format='scatterweighted', values='pitchclass')


