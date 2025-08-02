import streamlit as st
import pandas as pd

st.set_page_config(page_title="Campus Energy Audit", layout="wide")
st.title("🏫 Campus Energy Audit & Action Plan")

st.subheader("📋 Step 1: Enter Device Information")

# User input
device = st.text_input("Enter Device Name (e.g., Light, Fan, AC)")
wattage = st.number_input("Power Rating in Watts (W)", min_value=1)
quantity = st.number_input("Number of Devices", min_value=1)
hours = st.slider("Average Hours Used Per Day", 0, 24, 6)
days = st.slider("Number of Days Used in a Month", 0, 31, 30)

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = []

# Add to session data
if st.button("➕ Add to Audit Table"):
    energy_kwh = round((wattage * quantity * hours * days) / 1000, 2)
    st.session_state.data.append({
        "Device": device,
        "Wattage (W)": wattage,
        "Quantity": quantity,
        "Hours/Day": hours,
        "Days/Month": days,
        "Energy (kWh/Month)": energy_kwh
    })
    st.success(f"{device} added successfully!")

# Display data table
if st.session_state.data:
    st.subheader("🔍 Step 2: Audit Data Table")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)

    total_energy = df["Energy (kWh/Month)"].sum()
    st.info(f"⚡ Total Monthly Energy Consumption: **{total_energy} kWh**")

    # Export CSV
    if st.button("📤 Export Report"):
        df.to_csv("energy_data.csv", index=False)
        st.success("Report saved as `energy_data.csv` in project folder!")

    # Recommendations
    st.subheader("💡 Step 3: Smart Energy Recommendations")
    st.markdown("""
    - ✅ Replace CFL/Tubelight with LED bulbs.
    - ✅ Install motion-sensor lights in low-traffic areas.
    - ✅ Set timers for high-energy devices.
    - ✅ Regular maintenance of ACs and fans.
    - ✅ Switch off idle devices after hours.
    - ✅ Consider renewable sources like rooftop solar.
    """)

else:
    st.warning("No data added yet. Please enter device details above.")

# Footer
st.markdown("---")
st.caption("Created as part of 1M1B Green Internship | SDG 7, 12, 13")
