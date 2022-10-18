from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import subprocess
import shutil
import asyncio

app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    filename = file.filename
    with open('image.png', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    cmd = 'python detect.py --weights best.pt --conf 0.1 --source image.png'
    p = subprocess.Popen(cmd, shell=True)
    await asyncio.sleep(10)
    return FileResponse("runs/detect/exp/image.png")