def days_in_full_years(birthday):
    """
    Given my birthday in the format "DD-MM-YYYY", calculates how many days have passed
    during the whole years between my birth year and the current year (excluding both).

    """
    current_year = 2025

    # Split the birthday string and extract the birth year.
    parts = birthday.split("-")
    birth_year = int(parts[2])

    total_days = 0
    # Loop over each full year between birth_year and current_year
    for year in range(birth_year + 1, current_year):
        # Check if the year is a leap year
        # A year is leap if it is divisible by 400, or divisible by 4 and not by 100
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            total_days += 366
        else:
            total_days += 365
    return total_days


# Example :
birthday = "17-08-2003"
print("Days in full years:", days_in_full_years(birthday))
