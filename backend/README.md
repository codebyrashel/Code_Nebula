# Installation and Setup

## Pre-requisites

- Python 3.12 or higher
- pip

## Installation

- Install uv.

```bash
pip3 install uv
```

- If you are not in the backend directory, change to the backend directory.

```bash
cd backend
```

- Run uv.

```bash
uv init .
```
> This will make the project directory a uv project.

- Now install the dependencies.

```bash
uv add "fastapi[standard]" "uvicorn[standard]"
```

- And then make a new folder named `src` in the project directory.
- Inside make a new file named `app.py` inside the `src` folder.
- Now we can make the first route.

```python
# backend/src/app.py
from fastapi import FastAPI

app = FastAPI() # initialize FastAPI

@app.get("/") # Path to the root 
async def root():
    return {"message": "Server is alive!"} # must return a something

```

- Now, we use uvcorn to setup the server.

```python 
# backend/main.py

import uvicorn

def main():
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True) # setting up the server with uvicorn

if __name__ == "__main__":
    main()
```

- Now start the server.

```bash
uv run ./main.py
# or
uv run uvicorn src.app:app --reload
```

Go to `http://localhost:8000/` and `You can see the massage `Server is alive!` in your browser.