# from app.utils.music_theory import get_scale_notes, get_diatonic_chords

# def main(root_note="C", mode="double harmonic minor"):
#     notes = get_scale_notes(root_note, mode)
#     print(f"{root_note} {mode.capitalize()} scale notes:", notes)

#     chords = get_diatonic_chords(notes)
#     print(f"\nDiatonic chords in {root_note} {mode.capitalize()} mode:")
#     for idx, (chord_name, chord_notes) in enumerate(chords, 1):
#         print(f"Degree {idx}: {chord_name or 'Unknown'} - {chord_notes}")

#     return notes, chords

# if __name__ == "__main__":
#     main()

from app.modules.composition.ambient_phrase_builder import generate_ambient_progression
from app.modules.export.midi_exporter import save_progression_as_midi


mood = "calm"
result = generate_ambient_progression("C", mood, length=6, seed=5, pedal_tone="auto")
save_progression_as_midi(
    progression=result['progression'],
    root_note=result['root_note'],
    mode=result['mode'],
    mood=mood,
    pedal_tone=result['pedal_tone']
)