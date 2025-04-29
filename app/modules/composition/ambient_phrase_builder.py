from app.utils.music_theory import get_scale_notes, get_diatonic_chords
import random
from music21 import chord, pitch

MOOD_TO_MODES = {
    "calm": ["ionian", "lydian", "dorian"],
    "mysterious": ["phrygian", "locrian", "double harmonic minor", "ultraphrygian", "oriental"],
    "uplifting": ["mixolydian", "lydian #2 #6", "ionian #2 #5"],
}

MOOD_DEGREE_WEIGHTS = {
    "calm": [0, 3, 5],
    "mysterious": [1, 2, 5],
    "uplifting": [0, 4, 5],
}

def pick_mode_for_mood(mood, rng=None):
    if rng is None:
        rng = random
    return rng.choice(MOOD_TO_MODES[mood])

def add_chord_extension(m21_chord, rng):
    extensions = ["add2", "sus2", "sus4", "7"]
    ext = rng.choice(extensions)

    root = m21_chord.root()
    pitches = [p.nameWithOctave for p in m21_chord.pitches]

    if ext == "add2":
        extra = pitch.Pitch(root.name)
        extra.midi += 2
        m21_chord.add(extra)
    elif ext == "sus2":
        m21_chord = chord.Chord([root, root.transpose(2), root.transpose(7)])
    elif ext == "sus4":
        m21_chord = chord.Chord([root, root.transpose(5), root.transpose(7)])
    elif ext == "7":
        extra = root.transpose(10)
        m21_chord.add(extra)

    return m21_chord

def get_chord_root(ch):
    try:
        return ch.root().midi
    except:
        return ch.pitches[0].midi

def weighted_chord_selection(chords, preferred_degrees, length, rng=None, smooth=True):
    if rng is None:
        rng = random

    result = []
    last_root = None

    for _ in range(length):
        if rng.random() < 0.7:
            idx = rng.choice(preferred_degrees)
        else:
            idx = rng.randint(0, len(chords) - 1)

        next_chord = chords[idx]

        if smooth and last_root is not None:
            attempts = 0
            while abs(get_chord_root(next_chord) - last_root) > 5 and attempts < 5:
                idx = rng.randint(0, len(chords) - 1)
                next_chord = chords[idx]
                attempts += 1

        result.append(next_chord)
        last_root = get_chord_root(next_chord)

    return result

def ensure_start_end_chords(progression, chords, start_idx=0, end_idx=0):
    if progression:
        progression[0] = chords[start_idx]
        progression[-1] = chords[end_idx]
    return progression

def generate_ambient_progression(
    root_note, mood, length=4, seed=None,
    use_extensions=True, pedal_tone="auto",
    force_start_end=True
):
    rng = random.Random(seed) if seed is not None else random

    mode = pick_mode_for_mood(mood, rng)
    scale_notes = get_scale_notes(root_note, mode)
    chord_tuples = get_diatonic_chords(scale_notes)

    chords = []
    for _, ch in chord_tuples:
        if isinstance(ch, chord.Chord):
            chords.append(ch)
        elif isinstance(ch, list):
            chords.append(chord.Chord(ch))
        else:
            raise ValueError(f"Unexpected chord format: {type(ch)}")

    preferred_degrees = MOOD_DEGREE_WEIGHTS.get(mood, [0, 3, 5])

    progression = weighted_chord_selection(chords, preferred_degrees, length, rng)

    if force_start_end:
        progression = ensure_start_end_chords(progression, chords, start_idx=0, end_idx=0)

    if use_extensions:
        progression = [add_chord_extension(ch, rng) for ch in progression]

    pedal_tone_sequence = []
    if pedal_tone is not None:
        if pedal_tone == "auto":
            candidate_indices = [0, 1, 3, 4, 5] if len(scale_notes) > 5 else [0]
            current_base = scale_notes[random.choice(candidate_indices)]

            if hasattr(current_base, 'name'):
                current_base = current_base.name
            elif isinstance(current_base, str):
                current_base = current_base.strip('0123456789')

            for _ in range(length):
                if rng.random() < 0.3:
                    current_base = scale_notes[random.choice(candidate_indices)]
                    if hasattr(current_base, 'name'):
                        current_base = current_base.name
                    elif isinstance(current_base, str):
                        current_base = current_base.strip('0123456789')
                octave = rng.choice([2, 3])
                pedal_tone_sequence.append(f"{current_base}{octave}")
        else:
            pedal_tone_sequence = [pedal_tone] * length

    return {
        "root_note": root_note,
        "mode": mode,
        "progression": progression,
        "pedal_tone_sequence": pedal_tone_sequence
    }

if __name__ == "__main__":
    mood = "calm"
    result = generate_ambient_progression("C", mood, length=6, seed=5, pedal_tone="auto")
    print(f"Root: {result['root_note']}")
    print(f"Mode: {result['mode']}")
    print(f"Pedal Tone Sequence: {', '.join(result['pedal_tone_sequence'])}")
    print("Progression:")
    for idx, chord_obj in enumerate(result['progression']):
        note_names = [n.nameWithOctave for n in chord_obj.notes]
        print(f"{idx+1}: {chord_obj.commonName} -> {', '.join(note_names)}")