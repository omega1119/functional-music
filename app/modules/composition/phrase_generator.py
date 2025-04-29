import random
from app.utils.music_theory import get_scale_notes, get_diatonic_chords

def generate_chord_progression(root_note, mode, length=4, seed=None):
    if seed is not None:
        random.seed(seed)

    # Step 1: Get scale notes
    scale_notes = get_scale_notes(root_note, mode)

    # Step 2: Get diatonic chords
    chords = get_diatonic_chords(scale_notes)

    # Step 3: Randomly select chords for the progression
    progression = random.choices(chords, k=length)

    return progression

# Example usage
if __name__ == "__main__":
    progression = generate_chord_progression("C", "ionian", length=6)
    print("Generated Progression:")
    for idx, ch in enumerate(progression):
        print(f"{idx+1}: {ch}")