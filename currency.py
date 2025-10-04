from typing import Dict, Any

def format_output(api_result: Dict[Any, Any], amount: float) -> str:

    try:
        base_currency = api_result['base']
        date = api_result['date']
        rates = api_result['rates']
        target_currency = list(rates.keys())[0]
        rate = rates[target_currency]
        converted_amount = amount * rate
        inverse_rate = 1 / rate
        output = (f"The conversion rate on {date} from {base_currency} to {target_currency} "
                 f"was {rate:.4f}. So {amount:.2f} in {base_currency} correspond to "
                 f"{converted_amount:.2f} in {target_currency}. The inverse rate was {inverse_rate:.4f}.")
        
        return output
        
    except KeyError as e:
        return f"Error: Missing key in API result: {e}"
    except ZeroDivisionError:
        return "Error: Cannot calculate inverse rate - division by zero"
    except Exception as e:
        return f"Error formatting output: {e}"