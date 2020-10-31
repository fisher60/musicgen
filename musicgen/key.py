from typing import List, Optional

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

    def __str__(self):
        return str(self.root_note)

    @property
    def chromatic_scale(self) -> tuple:
        return tuple(Note(f"{x}{self.root_note.octave}") for x in Note.all_notes())


print(
    *[f"{x.name}{x.octave} | {x.frequency}" for x in Key("c2").chromatic_scale],
    sep="\n",
)
