from fastapi import FastAPI

app = FastAPI(title="sandbox")


@app.get("/")
async def root():
    return {"message": "Welcome to Sandbox"}

@app.post("/string_changer/{text}")
async def string_changer(text:str):
    text = text.swapcase()
    return {"message": text}