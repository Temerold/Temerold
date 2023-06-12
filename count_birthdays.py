from datetime import datetime, date, timedelta


def count_birthdays(
    end_date: date = datetime.now().date(),
    start_date: date = date(2008, 10, 15),
    month: int = 10,
    day: int = 15,
) -> int:
    """
    Counts the number of birthdays that fall on a specific month and day within
    a given range of dates.

    Args:
        end_date (datetime.date, optional): The end date of the range to count
            birthdays. Defaults to the current date.
        start_date (datetime.date, optional): The start date of the range to
            count birthdays in. Defaults to October 15, 2008.
        month (int): The month of the birthday to count. Defaults to October.
        day (int): The day of the birthday to count. Defaults to 15.

    Returns:
        int: The number of birthdays that fall on the specified month and day
            within the given range.

    Example:
        >>> from datetime import date
        >>> start_date = date(2008, 10, 15)
        >>> end_date = date(2023, 12, 31)
        >>> month = 10
        >>> day = 15
        >>> count = count_birthdays(end_date, start_date, month, day)
        >>> print(count)
        15

    In this example, the function `count_birthdays()` is used to count the
    number of birthdays that fall on October 15 within the range from October
    15, 2008, to December 31, 2023. The output is "15", indicating that there
    are "14" occurrences of birthdays on October 15 within the specified range.
    """
    count = 0
    while start_date <= end_date:
        if start_date.month == month and start_date.day == day:
            count += 1
        start_date += timedelta(days=1)
    return count - 1
