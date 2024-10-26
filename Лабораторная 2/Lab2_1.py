money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital
nowspend = spend
month = 0


while budget > 0:
    budget += salary - nowspend
    nowspend *= 1 + increase
    month += 1

#Так как цикл выйдет только когда появится долг, то последний месяц нам
#не подходит, значит возвращаем номер месяца без долга на предыдущий
actual_month = month - 1
print("Количество месяцев, которое можно протянуть без долгов:", actual_month)
