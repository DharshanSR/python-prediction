Progress = 0                       # opening a 0 variable to modify within the loop and calculate the total Progress
Trailer = 0                         # opening a 0 variable to modify within the loop and calculate the total module trailer  
Retriever = 0                     # opening a 0 variable to modify within the loop and calculate the total module Retriever
Exclude = 0                      # opening a 0 variable to modify within the loop and calculate the total Exclude
total = 0                           # opening a 0 variable to modify within the loop and calculate the total 

outcome = 0
outcomes = 0

# creating a empty list
all_credits = []
student_credits = []

def credits(Pass_MR,Defer_MR,Fail_MR,total):             #defining a function : it will tells python name of the function and if applicable what kind of information the function needs to  do its job
    global outcome
    if Pass_MR + Defer_MR + Fail_MR == 120:

        if Pass_MR == 120 and Defer_MR == 0 and Fail_MR == 0: 
            print("Progress")
            outcome = 'Progress'
            global Progress
            Progress += 1

        elif Pass_MR == 100 and (Defer_MR in(0, 20))and (Fail_MR in(0, 20)):
            print("Progress (module trailer)")
            outcome = 'Trailer'
            global Trailer
            Trailer += 1

        elif (Pass_MR in (0, 20, 40, 60, 80)) and (Fail_MR in (0, 20, 40, 60)):
            print("Do not progress-module retriever")
            outcome = 'Retriever'
            global Retriever
            Retriever += 1

        elif (Pass_MR in (40, 20, 0)) and (Defer_MR in (0, 20, 40)) and (Fail_MR in (80, 100, 120)):
            print("Exclude")
            outcome = 'Exclude'
            global Exclude
            Exclude += 1

    else:
        print('Total incorrect')


valid = True
while valid == True:
    while True:
        try:
            Pass_MR = int(input('\nPlease Enter Your Pass Marks : '))
            if (Pass_MR in [0,20,40,60,80,100,120]):
                break
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')

    while True:
        try:
            Defer_MR = int(input('Please Enter Your Defer marks : '))
            if (Defer_MR in [0,20,40,60,80,100,120]):
                break
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')


    while True:
        try:
            Fail_MR = int(input('Please Enter Your Fail Marks : '))
            if (Fail_MR in [0,20,40,60,80,100,120]):
                break
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')

    credits(Pass_MR,Defer_MR,Fail_MR,total)
    
    all_credits.append([outcome, Pass_MR, Defer_MR, Fail_MR])
    outcomes += 1

    correct= True
    while correct == True:
        print("\nWould you like to enter another set of data ?")
        option = input("Enter 'y' for Continue the programe or 'q' to Quit the programe and view results : ")

        if option == "y":
            correct = False
        elif option == "q":
            correct = False
            valid = False
        else:
            print("Plese Enter the Valid Input")
print()

print("-" * 150)
print("Histrogram")

print("Progress", Progress, ":", "*" * Progress)
print("Trailer", Trailer, ":", "*" * Trailer)
print("Retriever", Retriever, ":", "*" * Retriever)
print("Exclude", Exclude, ":", "*" * Exclude)

print()
print((Progress + Trailer + Retriever + Exclude), "Outcomes in toatal")

print()
print("-" * 100, "PART-02 LISTS OUTCOMES", "-" * 100)
print()

print("Part 02 :")

for i in range(0,len(all_credits)):            #using the for loop repeating for the number of count we get progress outcome 
    print(all_credits[i][0] , '-',  all_credits[i][1] , ',',  all_credits[i][2], ',', all_credits[i][3])       #acessing the elemnts of all the lists orderly
