import os
from fastapi import FastAPI, File, UploadFile, Form
from typing import Optional
from fastapi.responses import FileResponse
import requests

from .generate_ppt_content import generate_content
from .create_ppt import generate_ppt_from_template

app = FastAPI()


@app.post("/create_ppt/")
async def call_analyst_agent(
    topic: str = Form(...), 
    file: Optional[UploadFile] = File(None),
    analyst_ip: str = Form(None),
    analyst_port: str = Form(None)
):
    """
    Accepts topic and file input, calls the /analyst_agent/ endpoint, and returns a pptx file.

    Args:
        topic: The topic to be researched.
        file: An optional file to support the research.
        analyst_ip: The IP address of the Analyst Agent service.
        analyst_port: The port number of the Analyst Agent service

    Returns:
        FileResponse object: The generated PowerPoint presentation.
    """
    try:
        # Prepare the payload for the request
        data = {"topic": topic}
        files = None

        if file:
            files = {
                "file": (file.filename, file.file, file.content_type or "application/octet-stream")
            }

        # Make the POST request to the /analyst_agent/ endpoint
        response = requests.post(f"http://{analyst_ip}:{analyst_port}/analyst_agent/", params=data, files=files)
        
        content = generate_content(response.json()["raw"])

        generate_ppt_from_template(content.model_dump(), "template.pptx", "result.pptx")

        # Return the response from the /analyst_agent/ endpoint
        return FileResponse(path = os.path.abspath("final_result.pptx"), filename="result.pptx")

    except Exception as e:
        return {"error": str(e)}