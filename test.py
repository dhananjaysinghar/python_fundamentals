def add(num1, num2):
    print(f"Performing addition of {num1} & {num2}")
    return num1 + num2

def sub(num1, num2):
    print(f"Performing subtraction of {num1} & {num2}")
    return num1 - num2

def mul(num1, num2): 
    print(f"Performing multiplication of {num1} & {num2}")
    return num1 * num2

def div(num1, num2):
    print(f"Performing division of {num1} & {num2}")
    return num1 / num2


def math(num1, num2, operation):
    if operation < 1 or operation > 4:
        return -1
    if operation == 1:
        return add(num1, num2)
    elif operation == 2:
        return sub(num1, num2)
    elif operation == 3:
        return mul(num1, num2)
    else:
        return div(num1, num2)


try:
    number_1 = eval(input("Enter First Number : "))
    number_2 = eval(input("Enter Second Number : "))
    op_type = eval(input("Enter the operation add[1], sub[2], mul[3], div[4] : "))
    output = math(number_1, number_2, op_type)
    print(f"Output : {output}")
except Exception as ex:
    print("Error: ", ex)

