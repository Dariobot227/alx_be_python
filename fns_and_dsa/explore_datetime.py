from datetime import datetime, timedelta


def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()  # required variable name
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # return so Part 2 can reuse if needed


def calculate_future_date(days_to_add):
    """Calculate and display the future date after adding the given days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)  # required variable name
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")
    return future_date


def main():
    #displaying the current date first and time
    display_current_datetime()

    #grtting the future date
    #practsing good coding practises by using error handling
    days_input = input("Enter the number of days to add to the current date: ")

    try:
        days = int(days_input)
    except ValueError:
        raise ValueError("Invalid input. Please enter an integer number of days.")

    calculate_future_date(days)


if __name__ == "__main__":
    main()
