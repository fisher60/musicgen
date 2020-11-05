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

    def __str__(self):
        return str(self.root_note)

    @property
    def chromatic_scale(self) -> tuple:
        """
        Create the chromatic scale from the tuning frequency,
        then return the chromatic scale starting from the root of the key.
        """
        chrom_scale = tuple(
            Note(f"{x}{self.root_note.octave}") for x in Note.all_notes()
        )
        root_index = list(map(str, chrom_scale)).index(str(self.root_note))
        return tuple(chrom_scale[root_index:] + chrom_scale[:root_index])


# print(
#     *[f"{x.name}{x.octave} | {x.frequency}" for x in Key("c3").chromatic_scale],
#     sep="\n",
# )
