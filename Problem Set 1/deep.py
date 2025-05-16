def main():
    m = input("What is the Answer to the Great Question of Life, the Universe, and Everything: ").strip().lower()
    while(m != "42"  and m != "forty-two" and m != "forty two"):
        print("Nay")
        m = input("What is the Answer to the Great Question of Life, the Universe, and Everything: ")
    else:
        print("Yas")
main()