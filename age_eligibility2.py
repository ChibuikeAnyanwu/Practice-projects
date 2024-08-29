age = int(input("enter age of user: "))
match age:
    case 18:
        print("user is eligible to vote: ", age)
    case 21:
        print("user is eligible to drive: ", age)
    case 60:
        print("user is eligible to retire: ", age)

    case _:
        print("user is not eligible to vote: ", age)
        print("user is not eligible to drive: ", age)
        print("user is not eligible to retire: ", age)