import streamlit as st

st.set_page_config(page_title="Gas Calculation - Planimeter", layout="centered")

st.title("Gas Calculation Using Planimeter Reading")
st.write("Oil & Gas Field Application")

st.header("Input Data")

planimeter_area = st.number_input("Planimeter Area Reading", min_value=0.0, step=0.01)
x_scale = st.number_input("X-Scale (Time scale factor)", min_value=0.0, step=0.01)
y_scale = st.number_input("Y-Scale (Flow scale factor)", min_value=0.0, step=0.01)
time_hours = st.number_input("Total Chart Time (Hours)", min_value=0.0, step=0.1)

if st.button("Calculate Gas"):
    if planimeter_area > 0 and x_scale > 0 and y_scale > 0 and time_hours > 0:
        total_volume = planimeter_area * x_scale * y_scale
        avg_flow = total_volume / time_hours

        st.success("Calculation Completed")
        st.write(f"### Total Gas Volume = {total_volume:.2f}")
        st.write(f"### Average Flow Rate = {avg_flow:.2f} per hour")
    else:
        st.error("Please enter all values greater than zero.")
