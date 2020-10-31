from typing import Tuple


class Note:
    """
    Base class for a single note.

    Takes in the scientific pitch notation of a note, i.e 'c3' as a string
    """

    def __init__(self, pitch_notation: str, tuning_frequency: int = 440):
        self.pitch_notation = pitch_notation
        self.name, self.octave = self._validate_input()
        self.tuning_frequency = tuning_frequency
        self.frequency = self.calc_frequency()

    def __str__(self):
        return f"{self.name}{self.octave}"

    def _validate_input(self) -> Tuple[str, int]:
        """Checks that the input not is valid, then returns the """
        this_pitch_notation = self.pitch_notation.replace("#", "")
        note, octave = this_pitch_notation[0].upper(), int(this_pitch_notation[1:])

        if "#" in self.pitch_notation:
            note += "#"

        if octave < 0:
            raise ValueError("Octave cannot be below 0")

        return note, octave

    def calc_frequency(self) -> float:
        octave_diff = self.octave - 4
        dist_from_a = self.all_notes().index(self.name) - self.all_notes().index("A")
        n = len(self.all_notes()) * octave_diff + dist_from_a
        a = 2 ** (1 / 12)
        return round(self.tuning_frequency * (a ** n), 2)

    @staticmethod
    def all_notes() -> tuple:
        return "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
