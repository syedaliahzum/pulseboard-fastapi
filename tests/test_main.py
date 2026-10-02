from fastapi.testclient import TestClient
from app.main import app, projects, pulses

client = TestClient(app)

def setup_function():
    projects.clear()
    pulses.clear()

def test_project_pulse_summary():
    project = client.post("/projects", json={"name": "Launch", "owner": "Ammar"}).json()
    client.post(f"/projects/{project['id']}/pulses", json={"mood": 4, "blockers": ""})
    response = client.get(f"/projects/{project['id']}/summary")
    assert response.status_code == 200
    assert response.json()["health_score"] == 4.0
