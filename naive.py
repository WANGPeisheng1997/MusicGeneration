from main import generate_midi_list, generate_music_list
from module import Music, Track
import pickle


def get_freq_dict(pitch=True,length=False):
    midi_list = generate_midi_list()
    music_list = generate_music_list(midi_list)
    mat = {}
    fq = {}

    for music in music_list:
        if pitch and length:
            previous = 128,0
        elif pitch and not length:
            previous = 128

        track = music.get_single_track()
        for each_pitch in track.get_pitch_list():
            try:
                current = each_pitch
                if previous not in mat:
                    mat[previous]= {}
                if current not in mat[previous]:
                    mat[previous][current] = 0
                mat[previous][current] += 1
                previous = current
            except:
                pass

    for previous in mat:
        sum_row = sum(mat[previous][current] for current in mat[previous])
        for current in mat[previous]:
            mat[previous][current] /= sum_row
        fq[previous] = sorted(mat[previous],key=lambda x:-mat[previous][x])
        #print(mat[previous])
        print(previous, fq[previous])

    return mat,fq


def naive_short_music(mat,fq):
    return mat,fq


if __name__ == "__main__":
    mat,fq = get_freq_dict()
    naive_short_music(mat, fq)
