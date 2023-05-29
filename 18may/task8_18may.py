user_input = input("введите трехзначное число: ")
user_int = int(user_input)
x = (user_int//10) % 10
print("вывести вторую цифру числа:" , x)