Progress = 0            # opening a 0 variable to modify within the loop and calculate the total Progress
Trailer = 0               # opening a 0 variable to modify within the loop and calculate the total module trailer 
Retriever = 0           # opening a 0 variable to modify within the loop and calculate the total module Retriever
Exclude = 0             # opening a 0 variable to modify within the loop and calculate the total Exclude
total = 0                  # opening a 0 variable to modify eithin loop and calculate total

def credits(Pass_MR, Defer_MR, Fail_MR, total):                         #defining a function : it will tells python name of the function and if applicable what kind of information the function needs to  do its job
    
    if Pass_MR + Defer_MR + Fail_MR == 120: 

        if Pass_MR == 120 and Defer_MR == 0 and Fail_MR == 0:        # condition for print Progress
            print("Progress\n")
            global Progress 
            Progress = Progress + 1

        elif Pass_MR == 100 and (Defer_MR in(0, 20))and (Fail_MR in(0, 20)):           #condition for print module Trailer
            print("Progress (module trailer)\n")
            global Trailer
            Trailer = Trailer + 1

        elif (Pass_MR in (0, 20, 40, 60, 80)) and (Fail_MR in (0, 20, 40, 60)):              # condition for print module Retriever
            print("Do not progress-module retriever\n")
            global Retriever
            Retriever = Retriever + 1

        elif (Pass_MR in (40, 20, 0)) and (Defer_MR in (0, 20, 40)) and (Fail_MR in (80, 100, 120)):           #condition for print Exclude
            print("Exclude\n")
            global Exclude
            Exclude = Exclude + 1

    else:
        print('Total incorrect')       # if total is less than or greater than 120 print "Total Incorrecect"

# we are useing while loop if user needs to continue the program and get the credits of multiple students
valid = True
while valid == True:
    while True:
        try:                                                                      # useing try and except method to correct the Value error                                                                  
            Pass_MR = int(input('Please Enter Your Pass Marks : '))              # get the input from users
            if (Pass_MR in [0,20,40,60,80,100,120]):
                break
            else:           
                print('Out of range')
        except ValueError:
            print('Integer required')

    while True:
        try:                                                                            # useing try and except method to correct the Value error  
            Defer_MR = int(input('Please Enter Your Defer marks : '))           # get the input from users
            if (Defer_MR in [0,20,40,60,80,100,120]):
                break
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')


    while True:
        try:                                                                       # useing try and except method to correct the Value error  
            Fail_MR = int(input('Please Enter Your Fail Marks : '))                # get the input from users
            if (Fail_MR in [0,20,40,60,80,100,120]):
                break
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')

    credits(Pass_MR,Defer_MR,Fail_MR,total)                  # calling the def function

    correct= True
    while correct == True:
        print("\nWould you like to enter another set of data ?")
        option = input("Enter 'y' for Continue the programe or 'q' to Quit the programe and view results : ")    #getting the option input from user

        if option == "y":
            correct = False
        elif option == "q":
            correct = False
            valid = False
        else:
            print("Plese Enter Valid Input")

print()

print("-" * 150)
print("Histrogram") #print the histrogram
print()

print("Progress", Progress, ":", "*" * Progress)
print("Trailer", Trailer, ":", "*" * Trailer)
print("Retriever", Retriever, ":", "*" * Retriever)
print("Exclude", Exclude, ":", "*" * Exclude)

print()
print((Progress + Trailer + Exclude + Retriever), "Outcomes in toatal")

