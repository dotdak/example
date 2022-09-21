from repo.item_repo import db, Item


class ItemService:
    def get(self, id: int):
        return db.get(id)

    def create(self, item: Item):
        return db.create(item)

    def update(self, id: int, item: Item):
        return db.update(id, item)

    def delete(self, id: int):
        return db.delete(id)


item_service = ItemService()
