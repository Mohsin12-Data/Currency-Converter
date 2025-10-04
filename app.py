import streamlit as st
import datetime
from frankfurter import get_currencies, get_latest_rates, get_historical_rates
from currency import format_output

def main():
    """
    Main function to run the Streamlit currency converter app
    """
    st.title("Currency Converter")
    st.write("Convert currencies using real-time exchange rates from Frankfurter API")
    
    currencies = get_currencies()
    
    if not currencies:
        st.error("Unable to fetch currencies. Please check your internet connection.")
        return
    
    currency_list = sorted(list(currencies.keys()))
    

    col1, col2 = st.columns(2)
    
    with col1:

        amount = st.number_input(
            "Amount to convert:",
            min_value=0.01,
            value=100.0,
            step=0.01,
            format="%.2f"
        )
    
        from_currency = st.selectbox(
            "From Currency:",
            currency_list,
            index=currency_list.index("USD") if "USD" in currency_list else 0
        )
    
    with col2:
        st.write("")  # Empty space for alignment
        st.write("")  
        st.write("")  
        
   
        to_currency = st.selectbox(
            "To Currency:",
            currency_list,
            index=currency_list.index("EUR") if "EUR" in currency_list else 1
        )
    

    st.subheader("Latest Exchange Rate")
    
    if st.button("Get Latest Rate", type="primary"):
        if from_currency == to_currency:
            st.warning("Please select different currencies for conversion.")
        else:
            with st.spinner("Fetching latest rates..."):
                latest_data = get_latest_rates(from_currency, to_currency)
                
                if latest_data:
                    result = format_output(latest_data, amount)
                    st.success(result)
                else:
                    st.error("Unable to fetch latest exchange rates.")
    
    st.subheader("Historical Exchange Rate")
    
    # Date input
    max_date = datetime.date.today() - datetime.timedelta(days=1) 
    min_date = datetime.date(1999, 1, 4) 
    
    selected_date = st.date_input(
        "Select Date:",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )
    
    if st.button("Get Historical Rate"):
        if from_currency == to_currency:
            st.warning("Please select different currencies for conversion.")
        else:
            with st.spinner("Fetching historical rates..."):
                historical_data = get_historical_rates(from_currency, to_currency, selected_date)
                
                if historical_data:
                    result = format_output(historical_data, amount)
                    st.success(result)
                else:
                    st.error("Unable to fetch historical exchange rates for the selected date.")
    
    with st.expander("Available Currencies"):
        st.write("**Supported Currencies:**")
        for code, name in sorted(currencies.items()):
            st.write(f"**{code}**: {name}")

if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Currency Converter",
        page_icon="💱",
        layout="centered"
    )
    main()