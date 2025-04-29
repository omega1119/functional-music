import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.utils.music_theory import get_scale_notes, get_diatonic_chords

# === Example usage ===
root_note = "C"
mode = "double harmonic minor"  # try: "oriental", "hungarian major", etc.

notes = get_scale_notes(root_note, mode)
print(f"{root_note} {mode.capitalize()} scale notes:", notes)

chords = get_diatonic_chords(notes)
print(f"\nDiatonic chords in {root_note} {mode.capitalize()} mode:")
for idx, (chord_name, chord_notes) in enumerate(chords, 1):
    print(f"Degree {idx}: {chord_name or 'Unknown'} - {chord_notes}")