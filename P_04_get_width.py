# Ask for width and loop until they
# enter a number more than zero


error = "Please enter a number that is more than zero\n"
while True:
    try:
    # Ask user for a number
        width = float(input("Width: "))

        if width > 0:
            break
           # check if number is more than zero 
        else:
            print(error)

    except ValueError:
        print(error)