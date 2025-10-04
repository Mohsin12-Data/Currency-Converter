from api import call_api
from typing import Optional, Dict, Any
import datetime
BASE_URL = "https://api.frankfurter.app"

def get_currencies() -> Optional[Dict[str, str]]:
    """
    Function that will get the list of available currencies from the Frankfurter API
    
    Returns:
        Optional[Dict[str, str]]: Dictionary with currency codes as keys and names as values
                                 Returns None if API call fails
    """
    url = f"{BASE_URL}/currencies"
    
    try:
        result = call_api(url)
        return result
    except Exception as e:
        print(f"Error fetching currencies: {e}")
        return None

def get_latest_rates(from_currency: str, to_currency: str) -> Optional[Dict[Any, Any]]:
    """
    Function that will get the latest conversion rate between the provided currencies
    
    Args:
        from_currency (str): The base currency code (e.g., 'USD')
        to_currency (str): The target currency code (e.g., 'EUR')
        
    Returns:
        Optional[Dict[Any, Any]]: Dictionary containing conversion data including:
                                 - amount: Always 1 (base amount)
                                 - base: Base currency code
                                 - date: Date of the rates
                                 - rates: Dictionary with target currency and its rate
                                 Returns None if API call fails
    """
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}"
    
    try:
        result = call_api(url)
        return result
    except Exception as e:
        print(f"Error fetching latest rates: {e}")
        return None

def get_historical_rates(from_currency: str, to_currency: str, date: datetime.date) -> Optional[Dict[Any, Any]]:
    """
    Function that will get the historical conversion rate between the provided currencies for a specific date
    
    Args:
        from_currency (str): The base currency code (e.g., 'USD')
        to_currency (str): The target currency code (e.g., 'EUR')
        date (datetime.date): The date for which to get historical rates
        
    Returns:
        Optional[Dict[Any, Any]]: Dictionary containing conversion data including:
                                 - amount: Always 1 (base amount)
                                 - base: Base currency code
                                 - date: Date of the rates
                                 - rates: Dictionary with target currency and its rate
                                 Returns None if API call fails
    """
    # Format date as YYYY-MM-DD string
    date_str = date.strftime("%Y-%m-%d")
    url = f"{BASE_URL}/{date_str}?from={from_currency}&to={to_currency}"
    
    try:
        result = call_api(url)
        return result
    except Exception as e:
        print(f"Error fetching historical rates: {e}")
        return None