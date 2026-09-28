
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("logistic_model.pkl")

st.title("ABC Ltd. Delivery Prediction Tool")
st.write("Enter shipment details to predict whether the delivery will reach on time.")

# Inputs
warehouse = st.selectbox(
    "Warehouse Block",
    ["A", "B", "C", "D", "F"]
)

shipment = st.selectbox(
    "Mode of Shipment",
    ["Ship", "Flight", "Road"]
)

customer_calls = st.number_input(
    "Customer Care Calls",
    min_value=1,
    max_value=7,
    value=4
)

customer_rating = st.number_input(
    "Customer Rating",
    min_value=1,
    max_value=5,
    value=3
)

cost = st.number_input(
    "Cost of the Product",
    min_value=1,
    value=200
)

prior_purchases = st.number_input(
    "Prior Purchases",
    min_value=2,
    max_value=10,
    value=3
)

importance = st.selectbox(
    "Product Importance",
    ["low", "medium", "high"]
)

gender = st.selectbox(
    "Gender",
    ["F", "M"]
)

discount = st.number_input(
    "Discount Offered",
    min_value=1,
    max_value=65,
    value=10
)

weight = st.number_input(
    "Weight (gms)",
    min_value=1001,
    max_value=7846,
    value=4000
)

# Prediction button
if st.button("Predict Delivery Status"):

    input_data = pd.DataFrame({
        "Warehouse_block": [warehouse],
        "Mode_of_Shipment": [shipment],
        "Customer_care_calls": [customer_calls],
        "Customer_rating": [customer_rating],
        "Cost_of_the_Product": [cost],
        "Prior_purchases": [prior_purchases],
        "Product_importance": [importance],
        "Gender": [gender],
        "Discount_offered": [discount],
        "Weight_in_gms": [weight]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Prediction: Delivery is likely to reach ON TIME.")
    else:
        st.error("Prediction: Delivery is likely to be DELAYED.")
