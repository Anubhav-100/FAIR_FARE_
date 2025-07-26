# Home.py
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\ANUBHAV\Downloads\noida_cab_services_with_unique_timestamps.csv")
    return df

def show():
    st.markdown('<h1><img src="https://i.postimg.cc/rmdgtwQT/Screenshot-2025-07-24-193639-removebg-preview.png" alt="heading" class="img-head"></h1>', unsafe_allow_html=True)

    df = load_data()
    base_locations = sorted(df['pickup'].unique())

    locations_with_placeholder = ["Select Pickup Point"] + base_locations

    with st.container():
        col1, col2 = st.columns([2, 2]) 

        with col1:
            pickup = st.selectbox("Select Pickup Point", locations_with_placeholder, index=0, key="pickup")

        with col2:
            # Always show destination box with placeholder
            destination_options = ["Select Destination Point"] + (
                [loc for loc in base_locations if loc != pickup] if pickup != "Select Pickup Point" else []
            )
            destination = st.selectbox("Select Destination Point", destination_options, index=0, key="destination")

        st.markdown("<h2>🚗 Choose Cab Type</h2>", unsafe_allow_html=True)
        cab_type_options = ["Hatchback — 🚗", "Sedan — 🚘", "SUV — 🚙"]
        cab_type_full = st.radio("", cab_type_options, key="cab_type_radio")
        cab_type = cab_type_full.split(" — ")[0] if " — " in cab_type_full else cab_type_full

        st.markdown("")

        compare_col = st.columns([1, 1, 1])[1]  # center button
        with compare_col:
            if st.button("Compare Fare", use_container_width=False):

                # Validation
                if pickup == "Select Pickup Point" or destination == "Select Destination Point":
                    st.warning("⚠️ Please select both pickup and destination.")
                    return

                filtered_df = df[
                    (df['pickup'] == pickup) &
                    (df['destination'] == destination) &
                    (df['cab_type'] == cab_type)
                ]

                if not filtered_df.empty:
                    distance_km = round(filtered_df['distance_km'].iloc[0], 2)

                    st.markdown(
                        f"""
                        <p>📏 Distance: {distance_km} km <br>
                        💰 Fare Estimates:</p>
                        """,
                        unsafe_allow_html=True
                    )

                    for service in ['Ola', 'Uber', 'Rapido']:
                        fare = filtered_df[filtered_df['cab_service'] == service]['fare'].mean()
                        st.markdown(
                            f"<h3>🚖 <b>{service}:</b> ₹{round(fare, 2)}</h3>",
                            unsafe_allow_html=True
                        )

                else:
                    st.warning("⚠️ No fare data found for this route and cab type.")
