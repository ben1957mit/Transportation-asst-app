def total_volume(num, l, w, h):
    return (num * l * w * h) / 1728  # cubic feet

def pallets_per_row(trailer_width, pallet_width):
    return trailer_width // pallet_width

def rows_per_trailer(trailer_length, pallet_length):
    return trailer_length // pallet_length
def calculate_pallet_weight(
    pallet_tare_weight_lbs: float,
    cases_per_pallet: int,
    weight_per_case_lbs: float
) -> dict:
    """
    Returns total pallet weight and breakdown.
    """
    product_weight = cases_per_pallet * weight_per_case_lbs
    total_weight = pallet_tare_weight_lbs + product_weight

    return {
        "pallet_tare_weight_lbs": pallet_tare_weight_lbs,
        "cases_per_pallet": cases_per_pallet,
        "weight_per_case_lbs": weight_per_case_lbs,
        "product_weight_lbs": product_weight,
        "total_pallet_weight_lbs": total_weight,
    }
