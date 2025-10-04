import requests
import json
from typing import Optional, Dict, Any

def call_api(url: str) -> Optional[Dict[Any, Any]]:
    """
    Function that will call the Frankfurter API endpoint and return the result as a dictionary
    
    Args:
        url (str): The API endpoint URL to call
        
    Returns:
        Optional[Dict[Any, Any]]: JSON response as dictionary if successful, None if failed
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API. Check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while making the request: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Unable to parse JSON response.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None