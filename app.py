import streamlit as st
import pandas as pd

def calculate_table(pledge):
    admin_fee = 0.015 * pledge
    basic_20 = pledge - admin_fee
    higher_40 = basic_20 * 0.6
    additional_45 = basic_20 * 0.55
    
    data = {
        "Tax Band": ["Basic (20%)", "Higher (40%)", "Additional (45%)"],
        "Pledge (Payroll)": [pledge, pledge, pledge],
        "Admin Fee": [admin_fee, admin_fee, admin_fee],
        "Actual Cost": [basic_20, basic_20, basic_20],
        "Gift Aid": [basic_20 * 0.8, basic_20 * 0.8, basic_20 * 0.8],
        "You Give": [basic_20, basic_20, basic_20],
        "Cost (With Tax Relief)": [basic_20, higher_40, additional_45],
        "Cost (Without Tax Relief)": [basic_20, basic_20, basic_20]
    }
    return pd.DataFrame(data)

st.title("Payroll Giving Calculator")
pledge = st.number_input("Enter your payroll pledge:", min_value=1.0, value=10.0)

table = calculate_table(pledge)
st.dataframe(table)
