import streamlit as st

st.title("Ticket Price Calculator")

# Input controls
age = st.number_input("Enter Age", min_value=0, max_value=100, value=25)
show_time = st.selectbox("Show Time", ["Morning", "Evening"])
seat_type = st.selectbox("Seat Type", ["Premium", "Gold", "Standard"])
is_member = st.checkbox("Is Member?")
is_weekend = st.checkbox("Is Weekend?")
base_price = st.number_input("Base Price", min_value=0, value=20)

if st.button("Calculate Final Price"):
    # Discount logic
    discount = 3 if (is_member and age >= 21) else 0

    # Extra charges logic
    extra_charges = 2 if (is_weekend or show_time == "Evening") else 0

    # Service charges logic
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1

    # Final price calculation
    final_price = base_price + extra_charges + service_charges - discount

    st.success(f"Final price of ticket: ${final_price}")
    st.write(f"- Discount: ${discount}")
    st.write(f"- Extra Charges: ${extra_charges}")
    st.write(f"- Service Charges: ${service_charges}")
