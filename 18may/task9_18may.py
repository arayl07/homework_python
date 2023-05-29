number = int(input("Введите пятизначное число: "))

number = int(12345)
last_number = 12345 % 10

result_number = last_number * 10000 + number // 10

print("Новое число:", result_number)