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

    def get_pitch_list(self):
        return self.pitches

    def get_length_list(self):
        return self.lengths

    def get_pitch_with_index(self, index):
        return self.pitches[index]

    def get_lengths_with_index(self, index):
        return self.lengths[index]

    def get_note_count(self):
        return self.note_count

    def output_understandable_notes(self):
        for i in range(0, self.note_count):
            print('Note {}: Pitch {}, Length {}'.format(i, transfer_note2pitch(self.pitches[i]), self.lengths[i]/1024))


class Music:

    def __init__(self, number=-1, name=""):
        self.tracks = []
        self.number = number
        self.name = name

    def add_track(self, track):
        try:
            assert isinstance(track, Track)
            self.tracks.append(track)
        except:
            print("Type of track is wrong!")

    def get_single_track(self):
        return self.tracks[0]

    def get_total_notes(self):
        sum = 0
        for track in self.tracks:
            sum += track.get_note_count()
        return sum

    def get_total_lengths(self):
        sum = 0
        for track in self.tracks:
            for note in track.get_length_list():
                sum += note
        return sum

def transfer_note2pitch(note):
    transfer_dict = {0:'C', 1:'#C', 2:'D', 3:'bE', 4:'E', 5:'F', 6:'#F', 7:'G', 8:'#G', 9:'A', 10:'bB', 11:'B'}
    return transfer_dict[note%12] + str(int(note/12)-1)

def midi2music(file_name):
    midi = mido.MidiFile(file_name)
    music = Music(name=file_name)
    track = Track()

    for msg in midi.tracks[0]:
        if msg.type == 'note_off':
            track.add_note(msg.note, msg.time)

    music.add_track(track)
    return music