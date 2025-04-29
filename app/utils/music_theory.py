from music21 import scale, pitch, chord

# === Custom scale interval definitions ===
custom_modes = {
    'double harmonic minor': [0, 2, 3, 6, 7, 8, 11],
    'lydian #2 #6':          [0, 3, 4, 6, 7, 10, 11],
    'ultraphrygian':         [0, 1, 4, 5, 8, 9, 10],
    'hungarian major':       [0, 2, 4, 6, 7, 8, 11],
    'oriental':              [0, 1, 4, 5, 7, 9, 10],
    'ionian #2 #5':          [0, 3, 4, 5, 8, 9, 11],
    'locrian bb3 bb7':       [0, 1, 2, 5, 6, 8, 9]
}

# === Standard modes from music21 ===
builtin_modes = {
    'ionian': scale.MajorScale,
    'dorian': scale.DorianScale,
    'phrygian': scale.PhrygianScale,
    'lydian': scale.LydianScale,
    'mixolydian': scale.MixolydianScale,
    'aeolian': scale.MinorScale,
    'locrian': scale.LocrianScale,
}

def get_scale_notes(root_note: str, mode: str):
    """Returns the notes in the scale starting from the given root note."""
    mode = mode.lower()
    
    if mode in builtin_modes:
        scale_instance = builtin_modes[mode]()
        scale_instance.tonic = pitch.Pitch(root_note)
        return [str(scale_instance.pitchFromDegree(i)) for i in range(1, 8)]

    elif mode in custom_modes:
        root = pitch.Pitch(root_note)
        return [str(root.transpose(semi)) for semi in custom_modes[mode]]

    else:
        raise ValueError(f"Mode '{mode}' not supported.")

def get_diatonic_chords(notes):
    """Returns a list of triads for the given scale notes."""
    chords_list = []
    count = len(notes)
    for i in range(count):
        triad = [notes[i % count], notes[(i + 2) % count], notes[(i + 4) % count]]
        c = chord.Chord(triad)
        chord_name = c.commonName or "Unknown"
        chords_list.append((chord_name, triad))
    return chords_list

def list_supported_modes():
    """Returns a sorted list of all supported mode names."""
    return sorted(list(builtin_modes.keys()) + list(custom_modes.keys()))