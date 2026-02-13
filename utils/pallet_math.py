def total_volume(num, l, w, h):
    return (num * l * w * h) / 1728  # cubic feet

def pallets_per_row(trailer_width, pallet_width):
    return trailer_width // pallet_width

def rows_per_trailer(trailer_length, pallet_length):
    return trailer_length // pallet_length
