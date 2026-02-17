import streamlit as st
from utils.pallet_math import calculate_pallet_weight

st.set_page_config(page_title="Pallet Weight Calculator", layout="wide")

st.title("Pallet Weight Calculator")
st.write("Quickly estimate total pallet weight, including pallet tare and product weight.")

col1, col2 = st.columns(2)

with col1:
    pallet_tare_weight_lbs = st.number_input(
        "Pallet tare weight (lbs)",
        min_value=0.0,
        value=50.0,
        step=5.0,
        help="Weight of the empty pallet."
    )

    cases_per_pallet = st.number_input(
        "Cases per pallet",
        min_value=0,
        value=56,
        step=1,
        help="Total number of cases stacked on the pallet."
    )

with col2:
    weight_per_case_lbs = st.number_input(
        "Weight per case (lbs)",
        min_value=0.0,
        value=35.0,
        step=1.0,
        help="Gross weight of one case."
    )

st.markdown("---")

if st.button("Calculate pallet weight"):
    if cases_per_pallet <= 0 or weight_per_case_lbs <= 0:
        st.error("Please enter positive values for cases per pallet and weight per case.")
    else:
        result = calculate_pallet_weight(
            pallet_tare_weight_lbs=pallet_tare_weight_lbs,
            cases_per_pallet=cases_per_pallet,
            weight_per_case_lbs=weight_per_case_lbs,
        )

        st.subheader("Results")
        col_a, col_b = st.columns(2)

        with col_a:
            st.metric("Pallet tare weight (lbs)", f"{result['pallet_tare_weight_lbs']:.1f}")
            st.metric("Product weight (lbs)", f"{result['product_weight_lbs']:.1f}")

        with col_b:
            st.metric("Total pallet weight (lbs)", f"{result['total_pallet_weight_lbs']:.1f}")
            st.write(
                f"**Formula:** pallet tare ({result['pallet_tare_weight_lbs']:.1f}) "
                f"+ cases ({result['cases_per_pallet']} × {result['weight_per_case_lbs']:.1f})"
            )
