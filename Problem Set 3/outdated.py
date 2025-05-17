def main():
    while True:
        try:
            date = input("Enter a date: ")
            if "/" in date:
               month, day, year = date.split("/")
               month, day, year = int(month), int(day), int(year)

            elif "," in date:
                months = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]
                month_name, rest = date.split(" ", 1)
                day, year = rest.replace(",", "").split()
                if month_name not in months:
                    raise ValueError
                month = months.index(month_name)+1
                day = int(day)
                year = int(year)

            else:
                raise ValueError

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            print(f"{year:04}-{month:02}-{day:02}")
            break
        except (ValueError, IndexError):
            continue
main()