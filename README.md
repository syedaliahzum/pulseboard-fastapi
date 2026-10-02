# Pulseboard API

A production-minded FastAPI backend for a lightweight team pulse and project-health dashboard.

## Highlights

- JWT-ready authentication boundary and CORS configuration
- Typed Pydantic request/response models
- Project health scoring and weekly pulse check-ins
- SQLite for a zero-friction local start; SQLAlchemy data layer
- Tests, Dockerfile, health endpoint, and environment template

## Quick start

```bash
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for interactive API documentation.

## API surface

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/health` | Service readiness |
| GET/POST | `/projects` | List or create projects |
| POST | `/projects/{id}/pulses` | Submit a project pulse |
| GET | `/projects/{id}/summary` | Get current health summary |

## Quality

Run `pytest` before shipping. The project intentionally keeps domain logic in `app/services.py`, so moving from SQLite to Postgres is straightforward.

## License

MIT
