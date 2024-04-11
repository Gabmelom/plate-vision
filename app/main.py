from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn
import base64

from pathlib import Path
from scripts.detect_licenseplate import get_licenseplate_data

app = FastAPI()

app.mount("/static", StaticFiles(directory=Path(__file__).parent.absolute() / "static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    image = file.file.read()
    
    detected_image = get_licenseplate_data(image)
    
    if detected_image == -1:
        return {
            'success': 'false',
        }
    
    else:
        original = base64.b64encode(image).decode("utf-8")
        detected = base64.b64encode(detected_image).decode("utf-8")

        return {
            'success': 'true',
            "original_image": original,
            "detected_image": detected,
        }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)