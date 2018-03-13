from module import *
import os

midi_list = []
for root, dirs, files in os.walk("./melody", topdown=False):
    for name in files:
        if name.endswith(".mid"):
            midi_list.append(os.path.join(root, name))

music_list = []
for midi in midi_list:
    music_list.append(midi2music(midi))

for i, music in enumerate(music_list):
    print('Music {}: Notes {}, Length {}'.format(i + 1, music.get_notes(), music.get_lengths()))

#print(midi_list)