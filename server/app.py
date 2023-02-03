from fastapi import FastAPI

from server.routes.book_store_routes import router

app = FastAPI()

app.include_router(router, tags=["Student"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}