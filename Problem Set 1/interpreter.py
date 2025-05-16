def main():
    exp = input("Expression: ").strip().split()
    a = float (exp[0])
    b = float (exp[2])
    match exp[1]:
        case "+":
            print(a+b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case "-":
            print(a-b)


main()