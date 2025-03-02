import streamlit as st
import pandas as pd
import os
from io import BytesIO


def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ("Metre", "Centimetre"): 100,
        ("Centimetre", "Metre"): 0.01,
        ("Kilometre", "Metre"): 1000,
        ("Metre", "Kilometre"): 0.001,
        ("Inch", "Centimetre"): 2.54,
        ("Centimetre", "Inch"): 0.393701,
        ("Foot", "Metre"): 0.3048,
        ("Metre", "Foot"): 3.28084,
    }
    
    if (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]
    elif from_unit == to_unit:
        return value
    else:
        return None

st.title("Unit Converter")

units = ["Metre", "Centimetre", "Kilometre", "Inch", "Foot"]

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From unit:", units)
to_unit = st.selectbox("To unit:", units)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Conversion not available for selected units.")
