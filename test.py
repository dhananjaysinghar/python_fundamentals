def add(num1, num2):
    return num1 + num2



try:
    number_1 = eval(input("Enter First Number : "))
    number_2 = eval(input("Enter Second Number : "))
    output = add(number_1, number_2)
    print(f"Output : {output}")
except Exception as ex:
    print("Error: ", ex)


