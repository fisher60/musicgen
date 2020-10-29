from typing import Tuple


class Note:
    """
    Base class for a single note.

    Takes in the scientific pitch notation of a note, i.e 'c3' as a string
    """

    def __init__(self, pitch_notation: str):
        self.pitch_notation = pitch_notation
        self.name, self.octave = self._validate_input()

    def __str__(self):
        return f"{self.name}{self.octave}"

    def _validate_input(self) -> Tuple[str, int]:
        """Checks that the input not is valid, then returns the """
        note, octave = self.pitch_notation[0].upper(), int(self.pitch_notation[1:])
        if octave < 0:
            raise ValueError("Octave cannot be below 0")

        return note, octave
