from typing import TypedDict
import json

class InputParams(TypedDict):
    """
    入力パラメータ
    """
    year: int
    month: int

def now() -> InputParams:
    """
    Get the current year and month.

    Returns:
        InputParams: Current year and month.
    """
    from datetime import datetime
    now = datetime.now()
    return InputParams(year=now.year, month=now.month)

def load_from_json(json_str: str) -> InputParams:
    """
    Load input parameters from a JSON string.

    Args:
        json_str (str): JSON string containing the input parameters.

    Returns:
        InputParams: Parsed input parameters.
    """
    return json.loads(json_str)

if __name__ == "__main__":
    import sys
    import json

    # Read JSON input from stdin
    input_json = sys.stdin.read()

    # Load parameters from JSON
    params = load_from_json(input_json)

    # Print the loaded parameters
    print(f"Loaded parameters: {params}")

    # Example usage of the parameters
    print(f"Year: {params['year']}, Month: {params['month']}")