from dataclasses import field
from uuid import UUID


class Entity:
    id: UUID = field(hash=True)

    @classmethod
    def next_id(cls) -> UUID:
        return UUID.v4()
