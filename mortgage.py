principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
extra_months = 12
extra_all = extra_payment * extra_months
total_extra_paid = 0.0
total_paid = 0.0
count_month = 0


#сначала надо определить алгоритм рассчета тела долга с учетом дополнительных платежей
#для этого надо вычитать из тела долга допплатежи в обход обложения процента
#(так как это засчитывается как гашение долга)
#и делать это то количество месяцев, которое указано
#если количество месяцев стало ноль(проитерировать), далее эту "добавку" игнорить
#пока(итерация тело не станет = 0)
#тело

while principal > 0:
    if extra_all > 0:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        extra_all = extra_all - extra_payment
        count_month = count_month + 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        count_month = count_month + 1

print('Total paid', round(total_paid, 2))
print('Total count of months', count_month)