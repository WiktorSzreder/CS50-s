def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            x = int(fraction.split('/')[0])
            y = int(fraction.split('/')[1])

            if x > y or y == 0:
                raise ValueError

            percent = round((x / y) * 100)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break



        except (ValueError, ZeroDivisionError):
            print("Please enter a correct value.")
            continue



main()
