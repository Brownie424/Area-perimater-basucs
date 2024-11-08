# Ask for width and loop until they
# enter a number more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:
        try:
        # Ask user for a number
            width = float(input(question))

            if response > 0   :
                return response
               # check if number is more than zero
            else:
                print(error)

        except ValueError:
            print(error)

my_num = num_check("choose: ")