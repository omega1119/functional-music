from app.utils.music_theory import get_scale_notes, get_diatonic_chords

def main(root_note="C", mode="double harmonic minor"):
    notes = get_scale_notes(root_note, mode)
    print(f"{root_note} {mode.capitalize()} scale notes:", notes)

    chords = get_diatonic_chords(notes)
    print(f"\nDiatonic chords in {root_note} {mode.capitalize()} mode:")
    for idx, (chord_name, chord_notes) in enumerate(chords, 1):
        print(f"Degree {idx}: {chord_name or 'Unknown'} - {chord_notes}")

    return notes, chords

if __name__ == "__main__":
    main()