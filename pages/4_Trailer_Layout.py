import streamlit as st
from utils.layout_engine import generate_layout
from utils.pallet_math import pallets_per_row, rows_per_trailer
from utils.trailer_data import TRAILERS

st.title("Trailer Layout Visualizer")

trailer = st.selectbox("Select Trailer Type", list(TRAILERS.keys()))
pallet_w = st.number_input("Pallet Width (inches)", 48)
pallet_l = st.number_input("Pallet Length (inches)", 40)

t = TRAILERS[trailer]

cols = pallets_per_row(t["width"], pallet_w)
rows = rows_per_trailer(t["length"], pallet_l)

layout = generate_layout(rows, cols)

st.write("Layout Preview:")
for row in layout:
    st.write(" ".join(row))
