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

if __name__ == "__main__":
    board = generate_fretboard()

    print(board)