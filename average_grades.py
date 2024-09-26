def calculate_average(geometry, algebra, physics):
    return(geometry + algebra + physics) / 3

def main():
    try:
        geometry = float(input("enter your geometry grade: "))
        algebra = float(input("enter your algebra grade: "))
        physics = float(input("enter your physics grade: "))
    except ValueError:
        print("please return a valid number.")
        return

    if geometry < 0 or geometry > 10:
        print("geometry grade must be between 0 and 10.")
        return

    if algebra < 0 or algebra > 10:
        print("algebra grade must be between 0 and 10.")
        return

    if physics < 0 or physics > 10:
        print("physics grade must be between 0 and 10.")
        return

    average = calculate_average(geometry, algebra, physics)

    print(f"your average grade is: {average}")

    if average >= 7:
        print("Good job!")
    elif 4 <= average < 7:
        print("You need to work harder!")
    else:
        print("Failed, you really need to work harder!")

main()