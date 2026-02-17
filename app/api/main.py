from fastapi import FastAPI

app = FastAPI(title="Junior Dev Sim")

@app.get("/health")
def health():
	return {"status": "ok"}
