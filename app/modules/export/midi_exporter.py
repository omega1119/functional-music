from music21 import stream, midi, tempo, note, pitch
import datetime
import os
import copy

def save_progression_as_midi(progression, root_note, mode, mood, pedal_tone=None, filename=None, bpm=60, note_length=4.0, output_dir="."):
    """
    Save a chord progression and optional pedal tone as a multi-track MIDI file.

    Args:
        progression (list): List of music21 Chord objects.
        root_note (str): Root note of the progression.
        mode (str): Mode name used.
        mood (str): Mood category.
        pedal_tone (str or list, optional): Single note or list of pedal tones for each chord.
        filename (str, optional): Custom filename. If None, auto-generate based on mood/root/mode/timestamp.
        bpm (int): Tempo in beats per minute.
        note_length (float): Duration of each chord in quarter notes.
        output_dir (str): Directory to save the output MIDI file.
    """
    s = stream.Score()
    chord_part = stream.Part()
    pedal_part = stream.Part()
    chord_part.append(tempo.MetronomeMark(number=bpm))
    pedal_part.append(tempo.MetronomeMark(number=bpm))

    # Add chords to chord part
    for ch in progression:
        ch_copy = copy.deepcopy(ch)
        ch_copy.duration.quarterLength = note_length
        chord_part.append(ch_copy)

    s.append(chord_part)

    if pedal_tone:
        # If a list of tones, evolve pedal tone over time
        if isinstance(pedal_tone, list):
            for pt in pedal_tone:
                pedal_pitch = pitch.Pitch(pt)
                pedal_note = note.Note(pedal_pitch)
                pedal_note.duration.quarterLength = note_length
                pedal_part.append(pedal_note)
        else:
            # Single repeating pedal tone
            pedal_pitch = pitch.Pitch(pedal_tone)
            for _ in progression:
                pedal_note = note.Note(pedal_pitch)
                pedal_note.duration.quarterLength = note_length
                pedal_part.append(pedal_note)

        s.append(pedal_part)

    if filename is None:
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        safe_root = root_note.replace("#", "sharp").replace("b", "flat")
        safe_mode = mode.replace(" ", "-").replace("#", "sharp").replace("b", "flat")
        safe_mood = mood.replace(" ", "-").replace("#", "sharp").replace("b", "flat")
        filename = f"ambient_mood-{safe_mood}_root-{safe_root}_mode-{safe_mode}_{now}.mid"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)

    mf = midi.translate.streamToMidiFile(s)
    mf.open(filepath, 'wb')
    mf.write()
    mf.close()
    print(f"🎶 Saved multi-track MIDI file: {filepath}")

# Example standalone usage
if __name__ == "__main__":
    from app.modules.composition.ambient_phrase_builder import generate_ambient_progression

    mood = "calm"
    result = generate_ambient_progression("C", mood, length=6, seed=5, pedal_tone="auto")
    save_progression_as_midi(
        progression=result['progression'],
        root_note=result['root_note'],
        mode=result['mode'],
        mood=mood,
        pedal_tone=result['pedal_tone_sequence']
    )
