from music21 import converter, note, chord, pitch

# Generate fretboard mapping (EADGBE tuning, up to 20th fret)
def generate_fretboard():
    tuning = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']
    fretboard = {}
    for string_num, open_note in enumerate(tuning):  # 6 = low E
        base_pitch = pitch.Pitch(open_note)
        for fret in range(0, 18):
            note_name = base_pitch.transpose(fret).nameWithOctave
            if note_name not in fretboard:
                fretboard[note_name] = []
            fretboard[note_name].append((6 - string_num, fret))
    return fretboard

fretboard = generate_fretboard()

def midi_to_notes(midi_path):
    score = converter.parse(midi_path)
    notes = []
    for element in score.recurse().notes:
        if isinstance(element, note.Note):
            notes.append(element.pitch.nameWithOctave)
        elif isinstance(element, chord.Chord):
            for n in element.notes:
                notes.append(n.pitch.nameWithOctave)
    return notes

# Map note to (string, fret)
def note_to_tab(note_name, previous_string=None):
    if note_name not in fretboard:
        return None
    options = fretboard[note_name]
    if previous_string:
        # Prefer same or nearby string
        options = sorted(options, key=lambda x: abs(x[0] - previous_string))
    return options[0]  # pick the first viable option

# Convert full song
def midi_to_tab(midi_path):
    notes = midi_to_notes(midi_path)
    tab_sequence = []
    prev_string = None
    for n in notes:
        sf = note_to_tab(n, prev_string)
        if sf:
            tab_sequence.append(sf)
            prev_string = sf[0]
    return tab_sequence

# Print tab
def print_tab(tab_sequence):
    strings = {6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    for s, f in tab_sequence:
        for sn in strings:
            strings[sn].append(str(f) if sn == s else '-')
    for sn in range(1, 7):
        label = {1:'e', 2:'B', 3:'G', 4:'D', 5:'A', 6:'E'}[sn]
        print(label + "|" + "".join(strings[sn]) + "|")

# Example usage
def give_tab(filepath):
    midi_path = filepath  # <-- replace with your MIDI file
    tab = midi_to_tab(midi_path)
    print_tab(tab)

if __name__ == "__main__":
    give_tab("Mario Bros. - Super Mario Bros. Theme.mid")