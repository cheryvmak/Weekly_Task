# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.estimator import estimate_from_area

app = FastAPI(title="Tile Estimator - Manual")

class ManualRequest(BaseModel):
    length_m: float
    width_m: float
    tile_length_cm: float
    tile_width_cm: float
    waste_percent: float = 10
    tiles_per_box: int = 4
    cost_per_tile: float = 0.0

@app.post("/estimate_manual")
def estimate_manual(req: ManualRequest):
    floor_area = req.length_m * req.width_m
    resp = estimate_from_area(
        floor_area_m2=floor_area,
        tile_length_cm=req.tile_length_cm,
        tile_width_cm=req.tile_width_cm,
        waste_percent=req.waste_percent,
        tiles_per_box=req.tiles_per_box,
        cost_per_tile=req.cost_per_tile
    )
    return resp


# uvicorn app.main:app --reload --port 8000
