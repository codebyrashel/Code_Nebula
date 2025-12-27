import uvicorn

def main():
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True) # setting up the server with uvicorn

if __name__ == "__main__":
    main()
