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
    are 15 occurrences of birthdays on October 15 within the specified range.
    """
    count = 0
    while start_date <= end_date:
        # We add a day to `start_date` to avoid counting the first birthday in
        # one's life (not counting as a year)
        start_date += timedelta(days=1)
        if start_date.month == month and start_date.day == day:
            count += 1

    return count


if __name__ == "__main__":
    with open("README.md", "r") as file:
        lines = file.readlines()
    with open("README.md", "a") as file:
        file.truncate(0)
        first_line = lines[0]
        file.write(first_line)
        file.write(
            f"## Hi. I'm a {count_birthdays()}-year-old programmer from Sweden "
            ":)\n"
        )
        print(f"## Hi. I'm a {count_birthdays()}-year-old programmer from Sweden "
            ":)\n")

        for line in lines[2:]:
            file.write(line)
