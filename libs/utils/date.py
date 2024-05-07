import datetime

def get_time_stamp():
    """
    Generate a timestamp string with the current time.

    This function fetches the current time and formats it into a string with the format 'minute-hour-day-month-year'. 
    It is useful for creating unique identifiers based on the exact time of execution, such as for logging or naming files.

    Returns:
        str: A string representing the current time formatted as 'MM-HH-DD-MM-YYYY'.
    """
    # Get the current datetime
    current_time = datetime.datetime.now()

    # Format the datetime into a string with the desired structure
    return current_time.strftime("%H-%M-%d-%m-%Y")