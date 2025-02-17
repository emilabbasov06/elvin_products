from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import elektrik, santexnika, istilik, xirdavat, auth

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

app.include_router(auth.router)
app.include_router(elektrik.router)
app.include_router(santexnika.router)
app.include_router(istilik.router)
app.include_router(xirdavat.router)

@app.get('/')
async def index():
  return {'message': 'App Works! YAY!!!'}