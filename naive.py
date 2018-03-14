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
            last = 128,0
        elif pitch and not length:
            last = 128
        for line in str(music.get_single_track()).split("\n"):
            try:
                now = int(line.split()[3][:-1])
                if last not in mat:
                    mat[last]= {}
                if now not in mat[last]:
                    mat[last][now] = 0
                mat[last][now] += 1
                last = now
            except:
                pass
    for a in mat:
        summ = sum(mat[a][b] for b in mat[a])
        print(summ)
        for b in mat[a]:
            mat[a][b]/=summ
        fq[a] = sorted(mat[a],key=lambda x:-mat[a][x])
        print(mat[a])
        print(fq[a])
        if len(mat[a]) > 1:
            break
    return mat,fq


def naive_short_music(mat,fq):
    return mat,fq


if __name__ == "__main__":
    mat,fq = get_freq_dict()
    naive_short_music(mat, fq)
