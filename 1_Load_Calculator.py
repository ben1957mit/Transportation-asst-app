import streamlit as st
from utils.trailer_data import TRAILERS
from utils.pallet_math import total_volume

st.title("Load Calculator")

trailer = st.selectbox("Select Trailer Type", list(TRAILERS.keys()))
num_pallets = st.number_input("Number of Pallets", 0, 1000, 0)
pallet_l = st.number_input("Pallet Length (inches)", 40)
pallet_w = st.number_input("Pallet Width (inches)", 48)
pallet_h = st.number_input("Pallet Height (inches)", 60)

if st.button("Calculate Volume"):
    vol = total_volume(num_pallets, pallet_l, pallet_w, pallet_h)
    st.write(f"Total Volume: {vol:.2f} cubic feet")
