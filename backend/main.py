import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "math" / "linear_algebra"))

from linear_algebra import check_dependent
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class VectorGroup(BaseModel):
    vectors: list[list[float]]


@app.get("/")
def get_root():
    return {"message": "Hello from the backend"}

@app.post("/test-dependence")
def test_dependence(group: VectorGroup):
    result = check_dependent(*group.vectors)

    return {"dependence": result}