# Currency Converter Web App

**Student Name:** MD MOHSIN HIMEL MOZUMDER
**Student ID:** [25091885]

## Project Description

This project is a web-based currency converter application built using Python and Streamlit. The application fetches real-time and historical exchange rates from the Frankfurter API (https://www.frankfurter.app/) and provides users with an intuitive interface to convert between different currencies.

### Features

- **Real-time Currency Conversion**: Get the latest exchange rates between any two supported currencies
- **Historical Exchange Rates**: View exchange rates for any date since January 4, 1999
- **Interactive Web Interface**: User-friendly Streamlit interface with input validation
- **Comprehensive Currency Support**: Supports all currencies available through the Frankfurter API
- **Inverse Rate Calculation**: Automatically calculates and displays the inverse conversion rate
- **Error Handling**: Robust error handling for API failures and invalid inputs

## Project Structure

```
currency-converter/
│
├── app.py              # Main Streamlit application
├── api.py              # API communication functions
├── frankfurter.py      # Frankfurter API endpoint functions
├── currency.py         # Currency formatting functions
└── README.md          # Project documentation
```

## Python Functions

### app.py
- **main()**: Main function that runs the Streamlit application and manages the user interface

### api.py
- **call_api(url: str) → Optional[Dict[Any, Any]]**: Generic function to make HTTP requests to the Frankfurter API with error handling

### frankfurter.py
- **get_currencies() → Optional[Dict[str, str]]**: Fetches the list of available currencies from the API
- **get_latest_rates(from_currency: str, to_currency: str) → Optional[Dict[Any, Any]]**: Gets the latest conversion rate between two currencies
- **get_historical_rates(from_currency: str, to_currency: str, date: datetime.date) → Optional[Dict[Any, Any]]**: Gets historical conversion rates for a specific date

### currency.py
- **format_output(api_result: Dict[Any, Any], amount: float) → str**: Formats the API response and user input into the required output string format

## Installation Requirements

Make sure you have Python 3.7 or higher installed. Install the required packages using pip:

```bash
pip install streamlit requests
```

## Running the Application

1. **Download all project files** to a single directory
2. **Open terminal/command prompt** and navigate to the project directory
3. **Run the Streamlit app** using the following command:

```bash
streamlit run app.py
```

4. **Access the application** by opening your web browser and going to:
   ```
   http://localhost:8501
   ```

## Usage Instructions

1. **Enter Amount**: Input the amount you want to convert (minimum 0.01)
2. **Select Currencies**: Choose the source and target currencies from the dropdown menus
3. **Get Latest Rate**: Click the "Get Latest Rate" button to see current exchange rates
4. **Historical Rates**: Select a past date and click "Get Historical Rate" to see rates for that specific date
5. **View Results**: The conversion results will be displayed in the specified format

## API Endpoints Used

- **Currencies**: `https://api.frankfurter.app/currencies`
- **Latest Rates**: `https://api.frankfurter.app/latest?from={from}&to={to}`
- **Historical Rates**: `https://api.frankfurter.app/{date}?from={from}&to={to}`

## Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- Invalid API responses
- Invalid currency selections
- Invalid date selections
- Timeout errors
- JSON parsing errors

## Output Format

The application displays results in the following format:

```
The conversion rate on [date] from [from_currency] to [to_currency] was [rate]. 
So [amount] in [from_currency] correspond to [converted_amount] in [to_currency]. 
The inverse rate was [inverse_rate].
```

**Example:**
```
The conversion rate on 2023-07-10 from USD to EUR was 0.9120. 
So 100.00 in USD correspond to 91.20 in EUR. 
The inverse rate was 1.0965.
```

## Technical Notes

- The application uses the Frankfurter API which provides free, real-time exchange rate data
- Historical data is available from January 4, 1999
- All rates are based on data from the European Central Bank
- The application includes proper input validation and user feedback
- Responsive design works on desktop and mobile devices

## Dependencies

- **streamlit**: Web application framework
- **requests**: HTTP library for API calls
- **datetime**: Date handling (built-in Python module)
- **typing**: Type hints (built-in Python module)

---

