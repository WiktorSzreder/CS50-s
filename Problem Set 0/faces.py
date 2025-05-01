def main():
    text = input("Write something: ")
    newText = text.replace(":)","🙂").replace(":(","🙁")
    print(newText)

main()