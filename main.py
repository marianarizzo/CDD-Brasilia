from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("new_request.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/print", response_class=HTMLResponse)
async def print_page(request: Request):
    return templates.TemplateResponse("print.html", {"request": request})

@app.get("/street", response_class=HTMLResponse)
async def street(request: Request):
    return templates.TemplateResponse("street_detail.html", {"request": request})
