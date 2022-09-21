from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder

mock_db: dict[int, object] = {}


class Item(BaseModel):
    id: int | None
    name: str | None = Field(title="The name of the item",
                             max_length=100, min_length=1)
    description: str | None = Field(
        default=None, title="The description of the item",
        max_length=300, min_length=1
    )

    class Config:
        schema_extra = {
            "example": {
                "name": "foo",
                "description": "bar",
            }
        }


class Repo:
    def __init__(self) -> None:
        self.counter: int = 0

    def create(self, item: Item):
        self.counter += 1
        item.id = self.counter
        mock_db[self.counter] = jsonable_encoder(item)
        return item

    def get(self, id: int):
        return Item(**mock_db.get(id, {}))

    def update(self, id: int, item: Item):
        current_val = Item(**mock_db[id])
        update_data = item.dict(exclude_unset=True)
        updated_val = current_val.copy(update=update_data)
        print(current_val)
        print(updated_val)
        mock_db[id] = jsonable_encoder(updated_val)
        return updated_val

    def delete(self, id: int):
        return Item(**mock_db.pop(id, {}))


db = Repo()
