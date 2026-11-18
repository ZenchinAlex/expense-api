from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/expenses")
def expenses():
    return [
        {"category": "food", "amount": 100},
        {"category": "car", "amount": 150}
    ]