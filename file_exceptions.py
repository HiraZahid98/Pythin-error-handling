try:
    filename=input("Enter the filename to open?")
    with open(filename, "r") as f:
        read_data = f.read()
        print(read_data) 

except FileNotFoundError:
    print(f'Sorry the file {filename} doesnot exist')