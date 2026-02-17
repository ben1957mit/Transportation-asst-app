import streamlit as st
from utils.layout_engine import auto_place_pallets, draw_trailer_diagram

st.set_page_config(page_title="Trailer Diagram", layout="wide")

st.title("Trailer Loading Diagram")
st.write(
    "Visual guide for placing pallets to keep axle weights balanced and avoid overload."
)

st.markdown("### Enter pallet weights")

default_pallet_count = 10

num_pallets = st.number_input(
    "Number of pallets",
    min_value=1,
    max_value=30,
    value=default_pallet_count,
    step=1,
)

weights = []
cols = st.columns(5)
for i in range(num_pallets):
    col = cols[i % 5]
    with col:
        w = st.number_input(
            f"Pallet {i+1} weight (lbs)",
            min_value=0,
            value=1500,
            step=100,
            key=f"pallet_weight_{i}",
        )
        weights.append(w)

st.markdown("---")

if st.button("Generate loading diagram"):
    valid_weights = [w for w in weights if w > 0]

    if not valid_weights:
        st.error("Please enter at least one pallet with weight greater than 0.")
    else:
        pallets = auto_place_pallets(valid_weights)
        fig = draw_trailer_diagram(pallets)

        st.subheader("Recommended pallet placement")
        st.pyplot(fig)

        total_weight = sum(valid_weights)
        st.markdown("### Summary")
        st.write(f"**Total pallet weight:** {total_weight:,.0f} lbs")

        # Simple warning thresholds (you can tune these)
        if total_weight > 45000:
            st.error(
                "Total load is high. Verify axle weights on a scale to avoid overload."
            )
        elif total_weight > 40000:
            st.warning(
                "Load is moderately heavy. Pay close attention to axle distribution."
            )
        else:
            st.success("Total load is within a typical safe range for many operations.")

        st.markdown("#### Color legend")
        st.write("- **Green:** lighter pallets (< 1500 lbs)")
        st.write("- **Orange:** medium pallets (1500–1999 lbs)")
        st.write("- **Red:** heavy pallets (≥ 2000 lbs)")
        st.write(
            "- Blue shaded zone (middle): preferred area for heavier pallets (drive axles)."
        )
