import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_PROJECT_DIR = BASE_DIR.parent
TEMPLATE_DIR = ROOT_PROJECT_DIR / "html" # /var/www/html/
app = FastAPI()

templates = Jinja2Templates(directory=('/home/kali/dev/python-server/html'))


@app.get("/", response_class=HTMLResponse) # html -> localhost:8000/
def home(request:Request):
    return templates.TemplateResponse("index.nginx-debian.html", {"request": request, "title": "Jinja"})
