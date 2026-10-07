import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Ramesh Currency Converter",
    page_icon="💱",
    layout="centered"
)

# Title
st.title("💱 Ramesh Currency Converter")
st.write("Convert currencies quickly using live exchange rates.")

# Currency list
currencies = {
    "Indian Rupee (INR)": "INR",
    "US Dollar (USD)": "USD",
    "Euro (EUR)": "EUR",
    "British Pound (GBP)": "GBP",
    "Japanese Yen (JPY)": "JPY",
    "Australian Dollar (AUD)": "AUD",
    "Canadian Dollar (CAD)": "CAD",
    "Singapore Dollar (SGD)": "SGD"
}

# Amount
amount = st.number_input(
    "💰 Enter Amount",
    min_value=0.01,
    value=1.0,
    step=1.0
)

# Currency selection
col1, col2 = st.columns(2)

with col1:
    from_currency_name = st.selectbox(
        "From Currency",
        list(currencies.keys())
    )

with col2:
    to_currency_name = st.selectbox(
        "To Currency",
        list(currencies.keys()),
        index=1
    )

from_currency = currencies[from_currency_name]
to_currency = currencies[to_currency_name]

# Convert button
if st.button("🔄 Convert Currency", use_container_width=True):

    if from_currency == to_currency:
        converted_amount = amount

        st.success(
            f"💰 {amount:.2f} {from_currency} = "
            f"{converted_amount:.2f} {to_currency}"
        )

    else:
        try:
            url = (
                f"https://api.frankfurter.app/latest"
                f"?amount={amount}"
                f"&from={from_currency}"
                f"&to={to_currency}"
            )

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                converted_amount = data["rates"][to_currency]

                st.success(
                    f"💰 {amount:.2f} {from_currency} = "
                    f"{converted_amount:.2f} {to_currency}"
                )

                st.info(
                    f"📊 Exchange Rate: 1 {from_currency} = "
                    f"{converted_amount / amount:.4f} {to_currency}"
                )

            else:
                st.error("❌ Unable to fetch exchange rate.")

        except Exception as e:
            st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.caption("© 2026 Ramesh Currency Converter")