# handle exception
while True:
    try:
        num = float(input("Enter a number"))
        print(num)
        break
    except ValueError:
        print("Something went wrong")

