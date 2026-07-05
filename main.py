from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def healthCheck():
    return {'status':'Server is running!'}

