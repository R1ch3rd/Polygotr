from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
import schemas

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
 
@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers = ["*"],
)

@app.post("/translate",response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):
    task = crud.create_translation_task(x,y, ,p)
    background_tasks.add_task(perform_translation, task_id, request.text, request.languages, db)
    return {"task_id": {task.id}}
    # 40:00