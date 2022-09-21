import uvicorn
from fastapi import FastAPI, Path, Query, Header, Body
from service.item_service import item_service
from repo.item_repo import Item
from http import HTTPStatus
from pydantic import BaseModel
app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK)
async def get(*, user_agent: str | None = Header(default=None),
              q: str | None = Query(default=""),
              ):
    return {
        "message": "hello",
        "user_agent": user_agent,
        "q": q,
        # "body": body,
        # "kwargs": kwargs,
    }


@app.post("/", response_model=Item, status_code=HTTPStatus.CREATED)
async def create(item: Item):
    print(item)
    return item_service.create(item)


@app.get("/{id}", response_model=Item | None, status_code=HTTPStatus.OK)
async def get(id: int = Path(description="ID of item", gt=0)):
    return item_service.get(id)


@app.put("/{id}", response_model=Item | None, status_code=HTTPStatus.OK)
async def update(id:  int, item: Item):
    return item_service.update(id, item)


@app.delete("/{id}", response_model=Item | None, status_code=HTTPStatus.OK)
async def delete(id:  int = Path(description="ID of item", gt=0)):
    return item_service.delete(id)


if __name__ == "__main__":
    uvicorn.run("app:app")
