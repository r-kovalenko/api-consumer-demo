from fastapi import FastAPI

app = FastAPI(title="API Consumer Demo", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
