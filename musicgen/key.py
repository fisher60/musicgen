from typing import List, Optional

from musicgen.note import Note


class Key:
    def __init__(
        self, root_note: str, sequence: List[int] = None, key_name: str = None
    ):
        self.root_note = Note(root_note)

        if sequence is not None:
            self.sequence = sequence

        elif key_name is not None:
            raise NotImplementedError("Sequence is currently a required argument")

    def __str__(self):
        return str(self.root_note)


print(Key("a3"))
