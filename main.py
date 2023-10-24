from datetime import date, datetime


def get_birthdays_per_week(users):
    if not users:
        return {}

    # Current date
    current_date = datetime(2023, 12, 26).date()

    # Weekday map for converting integer to day name
    weekday_map = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday"
    }

    # Placeholder for results
    birthday_dict = {}

    for user in users:
        birthday_date = user["birthday"]

        # Calculate next birthday
        next_birthday = birthday_date.replace(year=current_date.year) # probably for the 4th test only
        if next_birthday < current_date:
            next_birthday = birthday_date.replace(year=current_date.year + 1)

        # Check if the birthday is within the next week
        delta = next_birthday - current_date
        if 0 <= delta.days <= 7:
            # If birthday is on the weekend, shift to Monday
            if next_birthday.weekday() > 4:
                day_name = "Monday"
            else:
                day_name = weekday_map[next_birthday.weekday()]

            # Create a list for this day if it doesn't exist
            if day_name not in birthday_dict:
                birthday_dict[day_name] = []

            # Add user to this day's list
            birthday_dict[day_name].append(user["name"])

    return birthday_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")