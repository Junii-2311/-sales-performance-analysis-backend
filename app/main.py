from fastapi import FastAPI
from app.routes import router

# Initialize FastAPI app
app = FastAPI()

# Include routes from the router
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Sales Team Performance API! Visit /docs for API documentation."}
