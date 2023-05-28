cost = float(input("введите стоимость покупки в долларах: "))
sale_percentage = float(input("введите размер скидки в долларах: "))

sale_amount = cost * sale_percentage / 100
total_amount = cost - sale_amount

print("Сумма покупки: %s" % cost) #%s вставить как строку
print("Скидка: %s" % sale_amount)
print("Сумма к оплате: %s" % total_amount)