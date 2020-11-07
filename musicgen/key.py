from typing import List

from musicgen.note import Note


class Key:
    def __init__(
        self,
        root_note: str,
        sequence: List[int] = None,
        key_name: str = None,
        tuning_frequency: int = 440,
    ):
        self.root_note = Note(root_note)
        self.tuning_frequency = tuning_frequency

        if sequence is not None:
            self.sequence = sequence

        elif key_name is not None:
            raise NotImplementedError("Sequence is currently a required argument")

        else:
            self.key = self.chromatic_scale

    def __str__(self):
        return "\n".join(map(str, self.key))

    @property
    def chromatic_scale(self) -> tuple:
        """
        Create the chromatic scale from the tuning frequency,
        then return the chromatic scale starting from the root of the key.
        """
        lower_notes = Note.all_notes()[Note.all_notes().index(self.root_note.note):]
        upper_notes = Note.all_notes()[: Note.all_notes().index(self.root_note.note)]
        upper_degree_offset = len(lower_notes)

        lower_octaves = [
            Note(f"{x}{self.root_note.octave}", degree=count + 1)
            for count, x in enumerate(lower_notes)
        ]

        upper_octaves = [
            Note(
                f"{x}{self.root_note.octave + 1}",
                degree=upper_degree_offset + count + 1,
            )
            for count, x in enumerate(upper_notes)
        ]

        return tuple(lower_octaves + upper_octaves)
