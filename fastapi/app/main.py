import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ip import get_ip

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_PROJECT_DIR = BASE_DIR.parent
TEMPLATE_DIR = ROOT_PROJECT_DIR.parent / "html"  # /var/www/html/
app = FastAPI()

templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@app.get("/", response_class=HTMLResponse)  # html -> localhost:8000/
def home(request: Request):
    return templates.TemplateResponse("index.nginx-debian.html",
                                      {"request": request, "title": "Jinja", "hostname": get_ip() })
