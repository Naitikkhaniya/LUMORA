from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth


app = FastAPI()
app.include_router(auth.router)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Lumora Backend Ready ✅"}
