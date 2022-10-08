while True:
    try:
        filename = input("Enter file name: ")
        with open(filename,"r") as f:
            print(f.read())
            break
    except FileNotFoundError:
        print(f"Sorry this file {filename} doesn;t exist")