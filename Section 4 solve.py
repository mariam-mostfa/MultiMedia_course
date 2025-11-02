def check_affortability():
    budget = int(input("enter your budget"))
    cost = int(input("enter the cost"))
    if cost <= budget:
        remaining = budget - cost
        print("affordable! you have" + str(remaining) + "left")
    else:
        needed = cost - budget
        print("Too expensive you need" + str(needed) + "more")


check_affortability()


# ******************************
def format_title():
    sentance = input("Enter the sentance")
    formatted_sentance = sentance.title()
    print("The formatted sentance is " + formatted_sentance)


format_title()


# *******************************
def sum():
    num1 = float(input("enter the number one "))
    num2 = float(input("enter the number two "))
    result = num1 + num2
    if result >= 100:
        print("result = " + str(result) + ":" + " it is greater than 100")
    else:
        print("result =" + str(result) + ":" + "it is smaller than 100")


sum()


# **********************************
def remove_from_list():
    my_list = ["Apple", "Banana", "Cherry", "Date"]
    print("original list : " + str(my_list))
    item_to_remove = input("Enter the item you want to remove:")
    if item_to_remove in my_list:
        my_list.remove(item_to_remove)
        print(str(item_to_remove) + " was successfully removed")
    else:
        print("Warning " + str(item_to_remove) + " was not found in the list")
    print("final list:" + str(my_list))


remove_from_list()


# ********************************
def calculate_factorial():
    N = int(input("Enter a positive integer: "))

    if N < 0:
        print("Factorial is not defined for negative numbers.")

    elif N == 0:
        print("The factorial of 0 is: 1")

    else:
        # هنا يتم تنفيذ الحساب الفعلي (ELSE) لأن N > 0
        result = 1

        # 4. Use a for loop to iterate from 1 up to N
        for number in range(1, N + 1):
            # 5. Multiply the current number by the current result.
            result *= number

        # 6. Print the final factorial value.
        print("The factorial of " + str(N) + "! is: " + str(result))


# Call the function to run the script
calculate_factorial()
