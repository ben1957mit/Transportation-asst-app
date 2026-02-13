import streamlit as st
from utils.pallet_math import pallets_per_row, rows_per_trailer
from utils.trailer_data import TRAILERS

st.title("Pallet Patterns")

trailer = st.selectbox("Select Trailer Type", list(TRAILERS.keys()))
pallet_w = st.number_input("Pallet Width (inches)", 48)
pallet_l = st.number_input("Pallet Length (inches)", 40)

t = TRAILERS[trailer]

cols = pallets_per_row(t["width"], pallet_w)
rows = rows_per_trailer(t["length"], pallet_l)

st.write(f"Pallets per row: {cols}")
st.write(f"Rows per trailer: {rows}")
st.write(f"Total pallets: {cols * rows}")
