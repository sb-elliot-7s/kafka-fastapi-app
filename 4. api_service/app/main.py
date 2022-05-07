from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import currency_router

app = FastAPI()

app.include_router(currency_router)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
