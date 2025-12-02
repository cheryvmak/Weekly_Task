# app/estimator.py
import math

DEFAULT_WASTE = 10    # percent
DEFAULT_TILES_PER_BOX = 4

def estimate_from_area(floor_area_m2, tile_length_cm, tile_width_cm,
                       waste_percent=None, tiles_per_box=None, cost_per_tile=0.0):
    """
    floor_area_m2: float area in square meters (e.g., length*width)
    tile_length_cm/tile_width_cm: tile size in centimeters (e.g., 60, 60)
    """
    waste = waste_percent if waste_percent is not None else DEFAULT_WASTE
    tiles_box = tiles_per_box if tiles_per_box is not None else DEFAULT_TILES_PER_BOX

    # Convert tile size cm->m and compute area of each tile in m^2
    tile_area_m2 = (tile_length_cm/100.0) * (tile_width_cm/100.0)

    # exact number of tiles (may be fractional)
    tiles_needed_exact = floor_area_m2 / tile_area_m2

    # add waste and round up to whole tiles
    tiles_with_waste = math.ceil(tiles_needed_exact * (1 + waste/100.0))

    # compute how many boxes (each box has tiles_box tiles)
    boxes_needed = math.ceil(tiles_with_waste / tiles_box)

    # cost
    total_cost = round(tiles_with_waste * cost_per_tile, 2)

    return {
        "floor_area_m2": round(floor_area_m2, 3),
        "tile_area_m2": round(tile_area_m2, 4),
        "tiles_needed_exact": round(tiles_needed_exact, 2),
        "tiles_with_waste": tiles_with_waste,
        "boxes_needed": boxes_needed,
        "total_cost": total_cost,
    }
