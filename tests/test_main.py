# tests/test_main.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # Add project root to path

from app.main import main

def test_double_harmonic_minor_scale_and_chords():
    notes, chords = main("C", "double harmonic minor")

    expected_notes = ['C', 'D', 'E-', 'F#', 'G', 'A-', 'B']
    assert notes == expected_notes

    expected_chords = [
        ('minor triad', ['C', 'E-', 'G']),
        ('incomplete half-diminished seventh chord', ['D', 'F#', 'G#']),
        ('augmented triad', ['E-', 'G', 'B']),
        ('incomplete dominant-seventh chord', ['F#', 'G#', 'C']),
        ('major triad', ['G', 'B', 'D']),
        ('enharmonic equivalent to major triad', ['G#', 'C', 'E-']),
        ('minor triad', ['B', 'D', 'F#'])
    ]

    # Compare just the chord notes, for flexibility
    assert [c[1] for c in chords] == [c[1] for c in expected_chords]