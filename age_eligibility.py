age = int(input("enter age of user: "))

if age >= 18 and age <= 20: 
    print("user is eligible to vote: ", age)
elif age >= 22 and age <= 25:
    print("user is eligible to drive: ", age)
elif age >= 50 and age <=60:
    print("user is eligible to retire: ", age)

else:
    print("user is not eligible to vote: ", age)
    print("user is not eligible to drive: ", age)
    print("user is not eligible to retire: ", age)


    