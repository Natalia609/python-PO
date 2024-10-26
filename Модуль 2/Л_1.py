money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
c =1
while (money_capital>=spend):
    c+=1
    if (c>2):
        spend+=spend*increase
    money_capital+=salary
    money_capital-=spend
print("Количество месяцев, которое можно протянуть без долгов:", c)
