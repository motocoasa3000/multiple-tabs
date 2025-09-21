# music_theory.py (continued)

def get_note_index(note_name):
    """
    Finds the position of a note in the CHROMATIC_NOTES list, ignoring octave.
    Example: get_note_index('C#') -> 1, get_note_index('Eb') -> 3 (But we use D#)
    """
    base_note = note_name[0]  # Get just the letter part (C, D, E, etc.)
    if len(note_name) > 1 and note_name[1] == 'b':
        # Handle flats by converting them to sharps for simplicity in our model.
        # This is a music theory logic decision! C# and Db are enharmonic equivalents.
        flat_to_sharp = {'Cb': 'B', 'Db': 'C#', 'Eb': 'D#', 'Fb': 'E', 'Gb': 'F#', 'Ab': 'G#', 'Bb': 'A#'}
        base_note = flat_to_sharp.get(note_name[:2], base_note) # Use the first two chars if it's a flat
    else:
        base_note = note_name # It's a natural or sharp

    try:
        return CHROMATIC_NOTES.index(base_note)
    except ValueError:
        raise ValueError(f"Note '{note_name}' is not a valid note name.")

def get_notes_in_scale(root_note, scale_type):
    """
    Generates the notes of a scale based on its formula.
    Example: get_notes_in_scale('C', 'major') -> ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    """
    if scale_type not in SCALE_FORMULAS:
        raise ValueError(f"Unknown scale type: {scale_type}")

    root_index = get_note_index(root_note)
    scale_intervals = SCALE_FORMULAS[scale_type]

    current_index = root_index
    scale_notes = [CHROMATIC_NOTES[root_index]] # Start with the root note

    for interval in scale_intervals:
        current_index = (current_index + interval) % len(CHROMATIC_NOTES)
        scale_notes.append(CHROMATIC_NOTES[current_index])

    return scale_notes

# Let's test our function immediately!
if __name__ == "__main__":
    # Quick test to see if our logic works
    print("C Major Scale:", get_notes_in_scale('C', 'major'))
    print("A Minor Pentatonic Scale:", get_notes_in_scale('A', 'minor_pentatonic'))
    print("Gb Major Scale:", get_notes_in_scale('Gb', 'major')) # Should handle flats