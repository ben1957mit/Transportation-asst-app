def generate_layout(rows, cols):
    layout = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("[X]")
        layout.append(row)
    return layout
