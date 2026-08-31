from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class DisallowAppPathMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/app"):
            return JSONResponse(status_code=403, content={"detail": "Access to /app routes is forbidden"})
        return await call_next(request)

app.add_middleware(DisallowAppPathMiddleware)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.get("/api/data")
async def get_data():
    return {"data": "some data"}