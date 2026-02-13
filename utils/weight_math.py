def weight_okay(total, max_allowed):
    return total <= max_allowed

def axle_split(total_weight):
    steer = total_weight * 0.12
    drive = total_weight * 0.43
    tandem = total_weight * 0.45
    return steer, drive, tandem
