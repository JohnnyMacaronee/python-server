import pathlib
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from ip import get_ip
from crud import get_entries, create_entry
from config import get_settings
from schema import EntryCreateSchema, EntryListSchema
from db import create_db_and_tables, get_db

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_PROJECT_DIR = BASE_DIR.parent
TEMPLATE_DIR = ROOT_PROJECT_DIR.parent / "html"  # /var/www/html/
app = FastAPI()
settings = get_settings()

templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

@app.on_event("startup")
def on_startup():
    print("starting...")
    create_db_and_tables()


@app.get("/", response_class=HTMLResponse)  # html -> localhost:8000/
def home(request: Request):
    return templates.TemplateResponse("index.nginx-debian.html",
                                      {"request": request, "title": "Jinja", "hostname": get_ip()})


@app.get("/abc")
def read_abc():
    return {"page": "abc", "db": settings.app_db is not None}


@app.get("/entries/", response_model=List[EntryListSchema])
def entry_list_view(db: Session = Depends(get_db)):
    return get_entries(db)


@app.post("/entries/", response_model=EntryCreateSchema, status_code=201)
def entry_create_view(data: EntryCreateSchema, db: Session = Depends(get_db)):
    #data = {"id": 1, "title": "hello world", "content": "abc"}
    return create_entry(db, data)
