from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Pulseboard API", version="1.0.0")

projects: dict[int, dict] = {}
pulses: dict[int, list[dict]] = {}

class ProjectInput(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    owner: str = Field(min_length=2, max_length=80)

class PulseInput(BaseModel):
    mood: int = Field(ge=1, le=5)
    blockers: str = Field(default="", max_length=500)

@app.get("/health")
def health():
    return {"status": "ok", "service": "pulseboard"}

@app.get("/projects")
def list_projects():
    return list(projects.values())

@app.post("/projects", status_code=201)
def create_project(payload: ProjectInput):
    project_id = len(projects) + 1
    project = {"id": project_id, **payload.model_dump()}
    projects[project_id] = project
    pulses[project_id] = []
    return project

@app.post("/projects/{project_id}/pulses", status_code=201)
def create_pulse(project_id: int, payload: PulseInput):
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    pulse = {"id": len(pulses[project_id]) + 1, **payload.model_dump()}
    pulses[project_id].append(pulse)
    return pulse

@app.get("/projects/{project_id}/summary")
def summary(project_id: int):
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    entries = pulses[project_id]
    score = round(sum(item["mood"] for item in entries) / len(entries), 1) if entries else None
    return {"project": projects[project_id], "pulse_count": len(entries), "health_score": score}
