from music21 import stream, midi, tempo, metadata
import datetime
import os

def save_progression_as_midi(progression, root_note, mode, mood, filename=None, bpm=60, note_length=4.0, output_dir="."):
    """
    Save a chord progression as a MIDI file with descriptive naming.

    Args:
        progression (list): List of music21 Chord objects.
        root_note (str): Root note of the progression.
        mode (str): Mode name used.
        mood (str): Mood category.
        filename (str, optional): Custom filename. If None, auto-generate based on mood/root/mode/timestamp.
        bpm (int): Tempo in beats per minute.
        note_length (float): Duration of each chord in quarter notes.
        output_dir (str): Directory to save the output MIDI file.
    """
    s = stream.Score()
    p = stream.Part()
    p.append(tempo.MetronomeMark(number=bpm))

    for ch in progression:
        ch.duration.quarterLength = note_length
        p.append(ch)

    s.append(p)

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
    print(f"🎶 Saved MIDI file: {filepath}")

# Example standalone usage
if __name__ == "__main__":
    from app.modules.composition.ambient_phrase_builder import generate_ambient_progression

    mood = "calm"
    result = generate_ambient_progression("C", mood, length=6)
    save_progression_as_midi(
        progression=result['progression'],
        root_note=result['root_note'],
        mode=result['mode'],
        mood=mood
    )
