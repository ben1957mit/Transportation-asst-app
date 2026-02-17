def generate_layout(rows, cols):
    layout = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("[X]")
        layout.append(row)
    return layout
import matplotlib.pyplot as plt
import matplotlib.patches as patches

TRAILER_LENGTH_IN = 636  # 53' trailer
TRAILER_WIDTH_IN = 102   # 102" wide
PALLET_LENGTH_IN = 48
PALLET_WIDTH_IN = 40

def auto_place_pallets(pallet_weights):
    """
    Simple auto-placement:
    - Sort pallets heaviest to lightest
    - Place heaviest near drive axles (roughly middle-back)
    - Fill forward and rear from there
    Returns list of pallet dicts: {x, y, length, width, weight}
    """

    # Zones (rough approximation in inches from nose)
    nose_zone_start = 0
    nose_zone_end = 144          # first 12'
    drive_zone_start = 144       # 12'
    drive_zone_end = 432         # 36'
    tail_zone_start = 432        # last 18'
    tail_zone_end = TRAILER_LENGTH_IN

    # Sort heaviest first
    sorted_weights = sorted(pallet_weights, reverse=True)

    pallets = []
    current_x_drive = drive_zone_start
    current_x_nose = nose_zone_start
    current_x_tail = tail_zone_start
    lane_y_positions = [0, PALLET_WIDTH_IN]  # two lanes side by side

    lane_index_drive = 0
    lane_index_nose = 0
    lane_index_tail = 0

    for w in sorted_weights:
        # Heavier pallets → drive zone first
        if current_x_drive + PALLET_LENGTH_IN <= drive_zone_end:
            pallets.append({
                "x": current_x_drive,
                "y": lane_y_positions[lane_index_drive],
                "length": PALLET_LENGTH_IN,
                "width": PALLET_WIDTH_IN,
                "weight": w,
            })
            lane_index_drive = 1 - lane_index_drive
            if lane_index_drive == 0:
                current_x_drive += PALLET_LENGTH_IN

        # Then nose
        elif current_x_nose + PALLET_LENGTH_IN <= nose_zone_end:
            pallets.append({
                "x": current_x_nose,
                "y": lane_y_positions[lane_index_nose],
                "length": PALLET_LENGTH_IN,
                "width": PALLET_WIDTH_IN,
                "weight": w,
            })
            lane_index_nose = 1 - lane_index_nose
            if lane_index_nose == 0:
                current_x_nose += PALLET_LENGTH_IN

        # Then tail
        elif current_x_tail + PALLET_LENGTH_IN <= tail_zone_end:
            pallets.append({
                "x": current_x_tail,
                "y": lane_y_positions[lane_index_tail],
                "length": PALLET_LENGTH_IN,
                "width": PALLET_WIDTH_IN,
                "weight": w,
            })
            lane_index_tail = 1 - lane_index_tail
            if lane_index_tail == 0:
                current_x_tail += PALLET_LENGTH_IN

        else:
            # No more room – ignore extras for now
            break

    return pallets


def draw_trailer_diagram(pallet_positions):
    """
    Draws a top-down trailer diagram with pallet positions.
    pallet_positions: list of dicts with keys:
        x, y, length, width, weight
    """

    fig, ax = plt.subplots(figsize=(12, 3))

    # Trailer outline
    trailer = patches.Rectangle(
        (0, 0),
        TRAILER_LENGTH_IN,
        TRAILER_WIDTH_IN,
        linewidth=2,
        edgecolor="black",
        facecolor="none",
    )
    ax.add_patch(trailer)

    # Axle zones (light shading)
    # Nose
    ax.add_patch(
        patches.Rectangle(
            (0, 0),
            144,
            TRAILER_WIDTH_IN,
            linewidth=0,
            facecolor="#f0f0f0",
            alpha=0.4,
        )
    )
    # Drive
    ax.add_patch(
        patches.Rectangle(
            (144, 0),
            288,
            TRAILER_WIDTH_IN,
            linewidth=0,
            facecolor="#e0f7fa",
            alpha=0.4,
        )
    )
    # Tail
    ax.add_patch(
        patches.Rectangle(
            (432, 0),
            TRAILER_LENGTH_IN - 432,
            TRAILER_WIDTH_IN,
            linewidth=0,
            facecolor="#fce4ec",
            alpha=0.4,
        )
    )

    # Pallets
    for pallet in pallet_positions:
        weight = pallet["weight"]
        if weight >= 2000:
            color = "#ef5350"  # heavy
        elif weight >= 1500:
            color = "#ffb74d"  # medium
        else:
            color = "#81c784"  # light

        rect = patches.Rectangle(
            (pallet["x"], pallet["y"]),
            pallet["length"],
            pallet["width"],
            linewidth=1,
            edgecolor="black",
            facecolor=color,
        )
        ax.add_patch(rect)
        ax.text(
            pallet["x"] + pallet["length"] / 2,
            pallet["y"] + pallet["width"] / 2,
            f'{weight:.0f}',
            ha="center",
            va="center",
            fontsize=7,
        )

    ax.set_xlim(0, TRAILER_LENGTH_IN)
    ax.set_ylim(0, TRAILER_WIDTH_IN)
    ax.set_aspect("equal")
    ax.axis("off")

    return fig
