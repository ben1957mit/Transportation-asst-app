import streamlit as st
from utils.trailer_data import TRAILERS

st.title("Trailer Comparison Tool")

st.write("Compare trailer dimensions and capacities side-by-side.")

trailer1 = st.selectbox("Select First Trailer", list(TRAILERS.keys()), key="t1")
trailer2 = st.selectbox("Select Second Trailer", list(TRAILERS.keys()), key="t2")

t1 = TRAILERS[trailer1]
t2 = TRAILERS[trailer2]

st.subheader("Comparison Results")

col1, col2 = st.columns(2)

with col1:
    st.write(f"### {trailer1}")
    st.write(f"Length: {t1['length']} ft")
    st.write(f"Width: {t1['width']} ft")
    st.write(f"Height: {t1['height']} ft")
    st.write(f"Max Weight: {t1['max_weight']} lbs")

with col2:
    st.write(f"### {trailer2}")
    st.write(f"Length: {t2['length']} ft")
    st.write(f"Width: {t2['width']} ft")
    st.write(f"Height: {t2['height']} ft")
    st.write(f"Max Weight: {t2['max_weight']} lbs")
