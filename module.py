import mido


class Track:

    def __init__(self):
        self.pitches = []
        self.lengths = []
        self.note_count = 0

    def add_note(self, note, time):
        self.pitches.append(note)
        self.lengths.append(time)
        self.note_count += 1

    def __str__(self):
        return_str = ""
        for i in range(0, self.note_count):
            return_str += 'Note {}: Pitch {}, Length {}'.format(i, self.pitches[i], self.lengths[i])
            return_str += '\n'
        return return_str

    def output_understandable_notes(self):
        for i in range(0, self.note_count):
            print('Note {}: Pitch {}, Length {}'.format(i, transfer_note2pitch(self.pitches[i]), self.lengths[i]/1024))


class Music:

    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        try:
            assert isinstance(track, Track)
            self.tracks.append(track)
        except:
            print("Type of track is wrong!")

    def get_single_track(self):
        return self.tracks[0]

    def get_notes(self):
        sum = 0
        for track in self.tracks:
            sum += track.note_count
        return sum

    def get_lengths(self):
        sum = 0
        for track in self.tracks:
            for note in track.lengths:
                sum += note
        return sum

def transfer_note2pitch(note):
    transfer_dict = {0:'C', 1:'#C', 2:'D', 3:'bE', 4:'E', 5:'F', 6:'#F', 7:'G', 8:'#G', 9:'A', 10:'bB', 11:'B'}
    return transfer_dict[note%12] + str(int(note/12)-1)

def midi2music(file_name):
    midi = mido.MidiFile(file_name)
    music = Music()
    track = Track()

    for msg in midi.tracks[0]:
        if msg.type == 'note_off':
            track.add_note(msg.note, msg.time)

    music.add_track(track)
    return music