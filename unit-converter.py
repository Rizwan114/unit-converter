import streamlit as st

st.title("Unit Converter App")
st.markdown("### Convert Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted results in real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, units):
    if category == "Length":
        if units == "Kilometers to Miles":
            return value * 0.621371
        elif units == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if units == "Kilograms to pounds":
            return value * 2.20462
        elif units == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if units == "Seconds to Minutes":
            return value / 60
        elif units == "Minutes to seconds":
            return value * 60
        elif units == "Minutes to hours":
            return value / 60
        elif units == "Hours to minutes":
            return value * 60
        elif units == "Hours to days":
            return value / 24
        elif units == "Days to hours":
            return value * 24
    return 0
        
if category == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to Minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")

    # completed
