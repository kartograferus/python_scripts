principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
extra_months = 12
extra_start_month = 61
extra_end_month = 108
#extra_all = extra_payment * extra_months
total_extra_paid = 0.0
total_paid = 0.0
count_month = 1
last_pay = 0.0

#сначала надо определить алгоритм рассчета тела долга с учетом дополнительных платежей
#для этого надо вычитать из тела долга допплатежи в обход обложения процента
#(так как это засчитывается как гашение долга)
#и делать это то количество месяцев, которое указано
#если количество месяцев стало ноль(проитерировать), далее эту "добавку" игнорить
#пока(итерация тело не станет = 0)
#пофиксил выпадение месяцев на +1
#пофиксил переплату в последний месяц, сделав проверку на размер оставшегося долга

while principal > 0 and principal > payment:
    if (count_month >= extra_start_month and count_month <= extra_end_month):
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        #extra_all = extra_all - extra_payment
        print (count_month, total_paid, principal, payment+extra_payment)
        count_month = count_month + 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        print(count_month, total_paid, principal, payment)
        count_month = count_month + 1

if principal < payment:
    last_pay = principal
    total_paid = total_paid + principal
    print (count_month, total_paid, principal, last_pay)

print('Total paid', round(total_paid, 2))
print('Total count of months', count_month)