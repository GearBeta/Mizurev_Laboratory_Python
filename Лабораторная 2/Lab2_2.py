salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
now_spend = spend

for _ in range(months):
    money_capital += now_spend - salary
    now_spend *= 1 + increase



print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
