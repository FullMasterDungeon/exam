income =int(input('введите сумму вклада: '))
percent = int(input('введите процент: '))
end_sum = int(input('введите желаемуе конечную сумму'))
time = 0
while income < end_sum:
    income = (percent/100/12)*income + income
    print(income)
    time += 1
print(time)