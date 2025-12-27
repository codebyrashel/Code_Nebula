from fastapi import FastAPI

app = FastAPI() # initialize FastAPI

@app.get("/") # Path to the root 
async def root():
    return {"message": "Server is alive!"} # must return a something