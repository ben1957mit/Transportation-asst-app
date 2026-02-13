import streamlit as st
from utils.trailer_data import TRAILERS
from utils.weight_math import weight_okay, axle_split

st.title("Weight Distribution")

trailer = st.selectbox("Select Trailer Type", list(TRAILERS.keys()))
total_weight = st.number_input("Total Freight Weight (lbs)", 0, 100000, 0)

max_w = TRAILERS[trailer]["max_weight"]

if st.button("Check Weight"):
    ok = weight_okay(total_weight, max_w)
    steer, drive, tandem = axle_split(total_weight)

    st.write(f"Within Limit: {ok}")
    st.write(f"Steer Axle: {steer:.0f} lbs")
    st.write(f"Drive Axle: {drive:.0f} lbs")
    st.write(f"Tandem Axle: {tandem:.0f} lbs")
